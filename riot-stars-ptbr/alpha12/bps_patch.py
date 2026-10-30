"""Standard BPS1 patch creation/application with all CRCs and bounded parsing.
Creator uses SourceRead/TargetRead; reader also supports overlapping copy actions.
"""
from pathlib import Path
import struct,zlib,json,argparse,hashlib

def number(n):
 if n<0:raise ValueError('negative number')
 out=bytearray()
 while True:
  x=n&127;n>>=7
  if not n:out.append(x|128);return bytes(out)
  out.append(x);n-=1

def create(source,target,metadata=b''):
 out=bytearray(b'BPS1'+number(len(source))+number(len(target))+number(len(metadata))+metadata)
 pending_type=None;pending_start=0;pending_length=0
 def flush():
  nonlocal pending_length
  if pending_length:
   out.extend(number(((pending_length-1)<<2)|pending_type))
   if pending_type==1:out.extend(target[pending_start:pending_start+pending_length])
   pending_length=0
 def run(mode,start,length):
  nonlocal pending_type,pending_start,pending_length
  if not length:return
  if pending_type!=mode:flush();pending_type=mode;pending_start=start
  if not pending_length:pending_start=start
  pending_length+=length
 pos=0;common=min(len(source),len(target));block=65536
 while pos<common:
  end=min(common,pos+block)
  if source[pos:end]==target[pos:end]:run(0,pos,end-pos);pos=end;continue
  start=pos;mode=int(source[pos]!=target[pos])
  while pos<end:
   newmode=int(source[pos]!=target[pos])
   if newmode!=mode:run(mode,start,pos-start);start=pos;mode=newmode
   pos+=1
  run(mode,start,pos-start)
 if len(target)>common:run(1,common,len(target)-common)
 flush();out.extend(struct.pack('<II',zlib.crc32(source),zlib.crc32(target)));out.extend(struct.pack('<I',zlib.crc32(out)))
 return bytes(out)

def apply(source,patch):
 if len(patch)<19 or patch[:4]!=b'BPS1':raise ValueError('not a BPS1 patch')
 if zlib.crc32(patch[:-4])!=struct.unpack_from('<I',patch,len(patch)-4)[0]:raise ValueError('patch CRC mismatch')
 source_crc,target_crc=struct.unpack_from('<II',patch,len(patch)-12)
 if zlib.crc32(source)!=source_crc:raise ValueError('incorrect original: source CRC mismatch')
 pos=4;limit=len(patch)-12
 def read():
  nonlocal pos
  value=0;shift=1
  for _ in range(10):
   if pos>=limit:raise ValueError('truncated number')
   x=patch[pos];pos+=1;value+=(x&127)*shift
   if x&128:return value
   shift<<=7;value+=shift
  raise ValueError('oversized number')
 source_size=read();target_size=read();meta_size=read()
 if source_size!=len(source):raise ValueError('incorrect original size')
 if target_size>1024*1024*1024:raise ValueError('output exceeds 1 GiB safety limit')
 pos+=meta_size
 if pos>limit:raise ValueError('truncated metadata')
 output=bytearray();source_relative=target_relative=0
 while len(output)<target_size:
  action=read();mode=action&3;length=(action>>2)+1
  if len(output)+length>target_size:raise ValueError('target overflow')
  if mode==0:
   start=len(output)
   if start+length>len(source):raise ValueError('source read out of bounds')
   output.extend(source[start:start+length])
  elif mode==1:
   if pos+length>limit:raise ValueError('literal out of bounds')
   output.extend(patch[pos:pos+length]);pos+=length
  else:
   delta=read();delta=(-1 if delta&1 else 1)*(delta>>1)
   if mode==2:
    source_relative+=delta
    if source_relative<0 or source_relative+length>len(source):raise ValueError('source copy out of bounds')
    output.extend(source[source_relative:source_relative+length]);source_relative+=length
   else:
    target_relative+=delta
    if target_relative<0 or target_relative>=len(output):raise ValueError('target copy out of bounds')
    for _ in range(length):output.append(output[target_relative]);target_relative+=1
 if pos!=limit:raise ValueError('unexpected patch data')
 if zlib.crc32(output)!=target_crc:raise ValueError('target CRC mismatch')
 return bytes(output)

def main():
 p=argparse.ArgumentParser(description=__doc__);sub=p.add_subparsers(dest='cmd',required=True)
 q=sub.add_parser('create');q.add_argument('original');q.add_argument('target');q.add_argument('patch')
 q=sub.add_parser('apply');q.add_argument('original');q.add_argument('patch');q.add_argument('output')
 a=p.parse_args();source=Path(a.original).read_bytes()
 if a.cmd=='create':
  target=Path(a.target).read_bytes();meta=json.dumps({'source_sha256':hashlib.sha256(source).hexdigest(),'target_sha256':hashlib.sha256(target).hexdigest(),'experimental':True}).encode()
  result=create(source,target,meta);destination=Path(a.patch)
 else:
  result=apply(source,Path(a.patch).read_bytes());destination=Path(a.output)
 if destination.resolve()==Path(a.original).resolve():raise ValueError('will not overwrite original')
 with destination.open('xb') as f:f.write(result)
 print(json.dumps({'output':str(destination),'bytes':len(result),'sha256':hashlib.sha256(result).hexdigest()}))
if __name__=='__main__':main()

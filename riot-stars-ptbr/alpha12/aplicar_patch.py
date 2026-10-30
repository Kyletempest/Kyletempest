"""Aplicador local: Python 3, sem pacotes externos. O BIN original não é alterado."""
from pathlib import Path
import sys,json,hashlib
from bps_patch import apply
ROOT=Path(__file__).resolve().parent

def aplicar(original,destino):
 original=Path(original);destino=Path(destino)
 manifest=json.loads((ROOT/'manifesto.json').read_text(encoding='utf-8'))
 source=original.read_bytes()
 if hashlib.sha256(source).hexdigest()!=manifest['source_sha256']:
  raise ValueError('O BIN não corresponde ao original japonês usado neste patch. Não use uma alpha anterior nem o ZIP.')
 if original.resolve()==destino.resolve():raise ValueError('Escolha outro nome para preservar o original.')
 cue=destino.with_suffix('.cue')
 if destino.exists() or cue.exists():raise ValueError('O arquivo de saída ou seu CUE já existe. Escolha outro nome.')
 result=apply(source,(ROOT/'Riot-Stars-PTBR-alpha12.bps').read_bytes())
 if hashlib.sha256(result).hexdigest()!=manifest['output_sha256']:raise ValueError('A verificação SHA-256 da saída falhou.')
 with destino.open('xb') as f:f.write(result)
 with cue.open('x',encoding='utf-8') as f:f.write(f'FILE "{destino.name}" BINARY\n  TRACK 01 MODE2/2352\n    INDEX 01 00:00:00\n')
 return cue

def main():
 if len(sys.argv)>1:
  original=sys.argv[1];destino=sys.argv[2] if len(sys.argv)>2 else str(ROOT/'Riot Stars PT-BR alpha12.bin')
  print('Pronto. Abra este CUE no emulador:',aplicar(original,destino));return
 import tkinter as tk
 from tkinter import filedialog,messagebox
 app=tk.Tk();app.withdraw()
 try:
  original=filedialog.askopenfilename(title='Selecione o BIN japonês ORIGINAL',filetypes=[('Imagem BIN','*.bin'),('Todos','*')])
  if not original:return
  destino=filedialog.asksaveasfilename(title='Salvar a cópia traduzida',initialfile='Riot Stars PT-BR alpha12.bin',defaultextension='.bin',filetypes=[('Imagem BIN','*.bin')])
  if not destino:return
  cue=aplicar(original,destino)
  messagebox.showinfo('Patch aplicado e verificado',f'Original preservado.\nAbra o CUE no emulador:\n{cue}\n\nA tradução é experimental e incompleta.')
 except Exception as e:messagebox.showerror('Não foi possível aplicar o patch',str(e))
 finally:app.destroy()
if __name__=='__main__':main()

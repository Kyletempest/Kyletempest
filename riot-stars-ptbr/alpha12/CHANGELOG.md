# Riot Stars PT-BR — histórico das versões

As versões são cumulativas. Aplique somente o patch mais recente ao BIN japonês original. Não aplique um patch sobre uma alpha anterior.

“Trecho inserido” significa que o texto foi traduzido e gravado no arquivo do jogo, com verificação dos limites e comandos. Isso não comprova que todas as rotas ou telas foram vistas no emulador. Um trecho pode conter várias falas ou páginas; não equivale a uma cena completa.

## Alpha12 — interface, vídeos e revisão em emulador

- Mais **42 trechos de batalha** traduzidos e inseridos; HEXMAP passa a 1.433 unidades de texto armazenado traduzidas, incluindo o material suplementar.
- **78 registros de rótulos gráficos** do HUD revisados: comandos, resultados, joias, habilidades, estatísticas e telas de batalha. Registros incluem variantes e não equivalem a 78 telas distintas.
- **41 registros gráficos** dos menus e minijogos localizados, incluindo corrida, caça-níqueis e cartas; placas SAÍDA e BEM-VINDO traduzidas.
- Imagem final passa a exibir **Obrigado por jogar!**, preservando os cartões de capítulos anteriores.
- Abertura: **102 quadros** editados, com nomes e chamadas localizados. Créditos: títulos de funções traduzidos em **844 quadros dos dez vídeos finais**; nomes pessoais da equipe mantêm a grafia original.
- Áudio, entrelaçamento, quantidade de quadros e setores não visuais dos vídeos preservados. Compressão recomposta nos limites dos quadros originais.
- Revisão real em PCSX-ReARMed com BIOS HLE: menu inicial, teclado latino, inserção de É, diálogos e chegada à primeira batalha. Não equivale a uma partida completa ou a um teste no DuckStation.
- A revisão revelou nomes de equipamento e habilidade sobrepostos e rótulos ASCII ainda em inglês na ficha. Inseridas formas curtas **Esp Rubra, Arm Couro e Dança**, além de ATAQUE, DEFESA, MÉRITO (exibido MERITO na fonte pequena) e abreviações de atributos.

Patch cumulativo para o BIN japonês original. Ainda é necessário testar todas as rotas, batalhas, salvamento e reprodução dos vídeos no DuckStation. Não há percentual global confiável de conclusão.

## Alpha11 — correção dos nomes na fonte pequena

- Corrigido o mapeamento da janela de unidade que desenhava minúsculas como números e símbolos. Exemplo comprovado na textura original: Sykes virava S9+%3.
- Nomes nessa fonte passam a usar maiúsculas verificadas: **SYKES, PIARIS, BANDIDO**. Acentos são simplificados somente nesse campo; a escrita dos diálogos permanece como antes.
- Alterados apenas 41 bytes da tabela de conversão em KOUSEI.EXE. Texturas, instruções, controles, tamanho do executável e demais traduções preservados.
- Verificação ampliada: saída do conversor MIPS ligada aos descritores reais e aos pixels da fonte, incluindo silhuetas independentes das letras. A hipótese anterior de que a tabela SJIS bastava para validar o desenho era incompleta.
- Relato do usuário: a tradução avançou bem no DuckStation no trecho testado, mas esse campo estava corrompido. Isso não confirma uma partida completa nem valida a alpha11 em execução.

Validação local: 46 testes e verificações do patch/disco. Confira os nomes das unidades ao iniciar ou carregar o jogo pela nova imagem; evite estados de emulador antigos, que mantêm o código anterior na memória.

## Alpha10 — integração dos catálogos e revisão de lacunas

- **838 trechos adicionais** do catálogo de batalha inseridos: deserto, canhão Ifrit, fortalezas, revelações sobre Highland, conspirações, ilhas e confrontos finais. O catálogo forte atual de HEXMAP fica com **1.245/1.245 unidades inseridas**.
- **134 trechos suplementares** recuperados fora do extrator antigo: respostas curtas, fragmentos com nomes e parágrafos legados. Alguns parágrafos têm execução ainda não demonstrada; são contados como texto armazenado traduzido, sem apresentá-los como cenas já testadas.
- **1.176 traduções únicas** de NPCs, itens, descrições e menus reescritas para caber nos espaços existentes. O roteiro principal passa de 6.370 para **8.929 ocorrências inseridas**, correspondentes a 2.143 textos únicos. Três listagens técnicas de assembly permanecem preservadas.
- **62 páginas de escolhas** revisadas, incluindo tutoriais, lojas, confirmações e seleção de depósito. Opções mantêm suas linhas e os espaços horizontais de SIM/NÃO. Treze sufixos após nomes dinâmicos foram identificados e inseridos.
- **271 ocorrências adicionais** de interface de batalha inseridas: terreno, condições de vitória/derrota, objetivos, habilidades e mensagens. Os catálogos de textos estáticos dos cinco executáveis agora somam **5.812 ocorrências inseridas**.
- Telas de cartão de memória traduzidas nos quatro módulos: verificação, formatação, carregar, salvar, confirmação, falta de espaço e erros. São 18 páginas distintas por módulo; posições do cursor e arquivos de save preservados.
- Mensagens fixas de KOUSEI traduzidas: limites de tempo, resgate de convidados, obtenção de itens, recompensas e diálogo de Sykes. Títulos externos de save usam Shift-JIS padrão, compatível com o navegador do PS1.
- **Cinco cartões gráficos de capítulos** traduzidos, com títulos completos em português e acentos. A arte ao redor, as paletas e os formatos originais são preservados; foi acrescentado um painel escuro na área das letras para cobrir o japonês.
- Todas as melhorias anteriores do título, teclado e nomes de unidades continuam incluídas.

Validação local: 43 testes, limites e comandos preservados, conferência dos setores do disco e reaplicação do BPS. As prévias são reconstruções dos recursos, não capturas de emulador. Esta é uma grande integração do material identificado, **ainda não uma certificação de tradução 100% do jogo**. Leia PENDENCIAS.md para o que falta, incluindo testes de rotas e a frase inglesa da imagem final.

## Alpha09 — continuação da história

**205 novos trechos inseridos**, em 287 páginas delimitadas pelas pausas originais. Total acumulado: 419 trechos de diálogos de batalha inseridos desde a alpha05.

- Igreja ocupada pelos orcs: confronto e resgate.
- Caviar: procura por Nakor, reencontro em Capela e despedida com flores e estrelas.
- Emboscada dos Cavaleiros Negros e intervenção de Ridge.
- Ordens de retaguarda, resgate de Seneca e investigação da fábrica de armas de Shelby.
- Fábrica: soldados mecânicos, prisioneiros e procura pelo pai de Seneca.
- Pântano sagrado: confronto e reconciliação com o povo-dragão.
- Floresta de Maya: encontro e decisão de perdoá-la, preservando a posição das duas opções.
- Caucasus: execução de Shiron, tentativa de resgate e diálogos alternativos.
- Leclerc: Cress, Irvine, libertação do rei e recrutamento de um soldado.
- Todas as mudanças das versões anteriores permanecem incluídas.

Validação local: 27 testes; limites por página, pausas, opções e dados fora dos textos preservados. BPS e setores do disco conferidos no empacotamento. Sem teste desta versão no emulador aqui; as cenas listadas precisam de confirmação em jogo, incluindo suas condições e rotas alternativas.

## Alpha08 — encontros seguintes e Floresta das Fadas

**153 novos trechos inseridos**, em 222 páginas. Total acumulado: 214 trechos de diálogos de batalha.

- Encontros após a abertura: hobbits, aliados e tropas imperiais.
- Resgate da princesa entre os orcs e cenas da Floresta das Fadas.
- Faye, Filis e Timmy: diálogos da aldeia, convite e despedida de Faye.
- Decisão de acompanhar Caviar até a igreja de Bernard.
- Falas alternativas para perdas e resultados de combate.
- Mantidas as correções da alpha07.

Validação local: 26 testes e integridade do patch. Sem confirmação de execução desta versão no emulador.

## Alpha07 — menu inicial, nome e fonte pequena

- Crédito alterado para **@2026 Traduzido em PTBR DDevian**, em amarelo e verde, abaixo do copyright original.
- Quatro opções iniciais traduzidas: RETOMAR PARTIDA, CARREGAR PARTIDA, NOVO JOGO e VOLTAR AO TÍTULO.
- Perguntas da tela de nome e SIM/NÃO traduzidos.
- Teclado latino: maiúsculas, minúsculas, números, acentos portugueses e pontuação. Seleção e gravação usam o mesmo código. Limite original de sete caracteres mantido.
- Conversor da fonte pequena dos nomes de unidades/inimigos corrigido para aceitar os códigos da tradução. Era separado do renderizador dos diálogos e produzia índices inválidos.

Validação local: 25 testes. Acentos dos nomes são simplificados na fonte pequena de batalha; diálogos mantêm a fonte com acentos. Aparência e navegação ainda precisam de confirmação no DuckStation.

## Alpha06 — título e Os Escarlates

- “Cav. Escarlates” substituído por **Os Escarlates** na abertura.
- PUSH START BUTTON substituído por **INICIAR**, preservando o piscar.
- Primeiro crédito **2026 DDevian** acrescentado abaixo de ©HECT1997. Posteriormente atualizado na alpha07.

Validação local: 20 testes. Prévia do título reconstruída dos recursos; não é captura de emulador.

## Alpha05 — diálogos reais da batalha inicial

- Localizado e incluído TACTICS/HEXMAP.BIN, ausente do catálogo anterior.
- **61 trechos da abertura** traduzidos e inseridos: perseguição, pedido de socorro, anel, Os Escarlates e tutoriais de batalha.
- **1.022 ocorrências de textos estáticos** inseridas em KOUSEI.EXE.
- Fonte de batalha instalada experimentalmente. O caminho dos nomes pequenos só recebeu sua correção específica na alpha07.

Limite técnico ainda relevante: a instalação da fonte utiliza uma rotina sem referências estáticas detectadas; chamadas indiretas calculadas não puderam ser completamente excluídas. Combates e transições precisam de teste real.

## Alpha04 — patch BPS e aplicador

- Distribuição em BPS, com aplicador Python, CUE e verificação do original.
- Incluídos os textos já inseridos em IMDATA/SCRIPT.BIN e quatro executáveis.
- **Teste relatado pelo usuário no DuckStation, com New Game:** apenas “Em meio à tempestade” apareceu em português; os textos antes e depois continuaram em japonês. Esse resultado levou à investigação e inclusão do roteiro de batalha na alpha05.

Os contadores antigos de reinserção não representavam a cobertura visível do jogo.

## Alpha02–Alpha03 — infraestrutura e primeiras integrações

- Extração, catálogo inicial, traduções de rascunho e reinserção experimental com limites fixos.
- Fonte com pares de caracteres latinos e suporte aos acentos portugueses.
- Ajustes de textos longos e geração das primeiras imagens para testes.

Este resumo agrupa a fase inicial: não há aqui um registro auditado suficiente para atribuir cada cena a uma dessas versões. A cronologia detalhada de conteúdo começa na alpha05. A tradução completa ainda está em andamento; a porcentagem global permanece desconhecida.

# Fernandes & Sá Advocacia

Site institucional do escritório Fernandes & Sá Advocacia (Direito Previdenciário, Ji-Paraná/RO).

Site estático em HTML, CSS e JavaScript puro: sem framework, sem etapa de build, sem banco de dados e sem chaves de API.

**Prévia:** <https://jonnathaleite.github.io/fernandes-sa-esboco/>

## Estrutura

```
.
├── index.html            Página inicial
├── guia-cnis.html        Guia e checklist do CNIS
├── privacidade.html      Política de privacidade (LGPD)
├── cookies.html          Política de cookies
├── assets/
│   ├── css/estilo.css    Estilos, organizados por seção (índice no topo do arquivo)
│   ├── js/
│   │   ├── banner.js       Carrossel do topo (pausa, gestos e teclado)
│   │   ├── duvidas.js      Central de dúvidas em vídeo (lista + player)
│   │   └── atendimento.js  Indicador "aberto/fechado" no rodapé
│   ├── img/              Logo, favicon, fotos e imagens do banner
│   ├── fontes/           DM Sans e Gelasio (WOFF2, licença OFL)
│   └── videos/           Vídeos das dúvidas frequentes e capas
└── ferramentas/
    └── videos/           Gerador dos vídeos (Python + FFmpeg)
```

## Rodar localmente

Qualquer servidor estático funciona. Com Python 3:

```sh
python -m http.server 8000
```

Depois, abra <http://localhost:8000>. No VS Code, a extensão **Live Server** faz o mesmo com um clique em "Go Live".

> Abrir o `index.html` direto pelo explorador de arquivos também funciona, mas os vídeos precisam de um servidor para avançar e voltar corretamente.

## Onde editar

| O que mudar                         | Onde                                                                 |
| ----------------------------------- | -------------------------------------------------------------------- |
| Textos, serviços e contatos         | `index.html`                                                         |
| Cores, fontes e espaçamentos        | Variáveis no início de `assets/css/estilo.css`                       |
| Horário do indicador aberto/fechado | Constantes `ABRE` e `FECHA` em `assets/js/atendimento.js`            |
| Fotos dos advogados                 | `assets/img/equipe/` (proporção 4:5, ex.: 480 × 600)                 |
| Perguntas e vídeos                  | `ferramentas/videos/perguntas.py` + seção `#duvidas` do `index.html` |

## Vídeos das dúvidas frequentes

Os vídeos são gerados a partir do conteúdo de `ferramentas/videos/perguntas.py`. Requisitos: Python 3, Pillow e FFmpeg.

```sh
python -m pip install Pillow
python ferramentas/videos/gerar_videos.py              # todos os vídeos
python ferramentas/videos/gerar_videos.py --only bpc   # apenas um
```

Use `--serif-font` e `--sans-font` para apontar arquivos `.ttf` se as fontes padrão não estiverem instaladas. Para substituir por vídeos gravados pelos advogados, basta manter o mesmo nome de arquivo em `assets/videos/`.

## Padrões do projeto

- Formatação com [Prettier](https://prettier.io) (`.prettierrc`) e [EditorConfig](https://editorconfig.org).
- Sem dependências externas em produção: fontes, vídeos e imagens são servidos pelo próprio site.
- Acessibilidade: navegação por teclado, foco visível, textos alternativos e respeito a `prefers-reduced-motion`.
- Conteúdo dentro das regras de publicidade da OAB (Provimento nº 205/2021): informativo, sem promessa de resultado.

## Publicação

Qualquer hospedagem estática serve (GitHub Pages, Netlify, Vercel, Hostinger etc.): publique a raiz do repositório. A pasta `ferramentas/` não é necessária em produção.

Ao trocar de hospedagem, atualize a menção ao provedor na seção 6 de `privacidade.html`.

## Pendências antes da versão final

- [ ] Razão social, CNPJ e encarregado (LGPD) em `privacidade.html` (marcados como "a preencher").
- [ ] Fotos oficiais dos advogados.
- [ ] Revisão jurídica das políticas e das respostas pelos advogados do escritório.

---

Desenvolvido por JL Tecnologia.

# Workflow And Install Guide

This file explains how Shui Pretty PPT is written, installed, updated, and validated.

## How This Skill Is Written

The skill uses progressive disclosure:

```text
shui-pretty-ppt/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── intake-and-density.md
│   ├── ppt-template-catalog.md
│   ├── quality-checklist.md
│   ├── editable-delivery.md
│   ├── workflow-and-install.md
│   ├── style-index.md
│   └── <template-reference>.md
├── scripts/
│   ├── copy_template.py
│   ├── inject_edit_mode.py
│   └── validate_deck.py
└── assets/templates/<style-slug>/index.html
```

### SKILL.md

The entrypoint. It should stay short enough for an agent to read quickly:

- what the skill does
- when to use it
- mode detection
- intake and density rules
- template selection
- copy/build/verify workflow
- list of supporting files

### references/

Long instructions live here. The agent reads only the relevant reference file:

- `intake-and-density.md`: questions, density, document-to-deck compression
- `ppt-template-catalog.md`: 12-template selection guide
- `quality-checklist.md`: final QA
- `editable-delivery.md`: browser edit mode and handoff rules
- one reference file per template

### assets/templates/

Each template has a complete runnable `index.html`. A generated deck starts by copying this folder.

### scripts/

Use scripts for repeatable actions:

- `copy_template.py`: copy a template to a target folder
- `inject_edit_mode.py`: add browser edit mode to an existing HTML deck
- `validate_deck.py`: check common output problems before delivery

## Install From GitHub

Recommended:

```bash
npx -y skills@latest add XshuiAi/shui-pretty-ppt \
  --skill shui-pretty-ppt \
  --agent codex \
  --global
```

Use `--copy` if symlinks are not desired:

```bash
npx -y skills@latest add XshuiAi/shui-pretty-ppt \
  --skill shui-pretty-ppt \
  --agent codex \
  --global \
  --copy \
  -y
```

## Manual Install

```bash
mkdir -p ~/.codex/skills
cp -R skills/shui-pretty-ppt ~/.codex/skills/shui-pretty-ppt
```

Then restart Codex if the skill list does not refresh.

## Verify Install

```bash
npx -y skills@latest list --global --agent codex --json
test -f ~/.agents/skills/shui-pretty-ppt/SKILL.md
```

If installed manually to `~/.codex/skills`, check:

```bash
test -f ~/.codex/skills/shui-pretty-ppt/SKILL.md
```

## Update Published Skill

After editing the repository:

```bash
git status --short
git add .
git commit -m "Improve Shui Pretty PPT workflow"
git push
```

Then reinstall/update locally:

```bash
npx -y skills@latest add XshuiAi/shui-pretty-ppt \
  --skill shui-pretty-ppt \
  --agent codex \
  --global \
  --copy \
  -y
```

## Validate A Template Copy

```bash
python3 skills/shui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force
python3 skills/shui-pretty-ppt/scripts/validate_deck.py /tmp/shui-cobalt-demo
open /tmp/shui-cobalt-demo/index.html
```

## Create An Editable Deck

Use this when the user needs to revise wording after generation, hand the deck to a client, or record a video showing that the result is not frozen.

```bash
python3 skills/shui-pretty-ppt/scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force --editable
open /tmp/shui-cobalt-demo/index.html
```

For an existing deck:

```bash
python3 skills/shui-pretty-ppt/scripts/inject_edit_mode.py /tmp/shui-cobalt-demo/index.html
```

Keyboard and toolbar behavior:

- Press `E` to enter or exit edit mode.
- Click text directly to edit it.
- Press `Cmd+S` / `Ctrl+S`, or click `保存`, to save changes to browser localStorage.
- Click `导出 HTML` to download a standalone edited HTML file.
- Click `重置` to clear local browser edits.

## Prompt Examples

Use automatic selection:

```text
使用 $shui-pretty-ppt，把这份文档做成一个适合分享的 HTML 网页 PPT。
请先判断内容密度和模板方向，再开始生成。
```

Specify a module:

```text
使用 $shui-pretty-ppt，做一个偏行政汇报的网页 PPT。
内容密度可以高一点，但不要堆满文字。
```

Specify a template:

```text
使用 $shui-pretty-ppt 的 Garden Pop Landing / 花园跳色长页，
把这个课程介绍做成更适合自媒体发布的 PPT。
```

Editable handoff:

```text
使用 $shui-pretty-ppt，把这份飞书文档做成可直接演示的 HTML 网页 PPT。
请开启可编辑模式，这样我录视频时可以展示直接修改页面文字和导出 HTML。
```

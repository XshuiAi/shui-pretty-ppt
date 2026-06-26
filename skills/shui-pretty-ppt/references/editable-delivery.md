# Editable Delivery

Use this reference when the user asks how a generated HTML web PPT can be revised after the first generation, or when the deck is meant for client handoff, video recording, workshops, or repeated polishing.

## What Editable Mode Solves

Generated HTML PPT is valuable because it can be opened and presented immediately. The weak point is that non-technical users may still want to change wording after generation. Shui Pretty PPT handles this with a lightweight browser edit layer:

- Press `E` to enter or exit edit mode.
- Click text directly to revise headings, paragraphs, list items, table cells, captions, and elements marked with `data-editable`.
- Press `Cmd+S` / `Ctrl+S`, or click `保存`, to save edits to the current browser.
- Click `导出 HTML` to download a standalone edited HTML file.
- Click `重置` to clear local saved edits.

This does not replace agent-based structural editing. It is for fast wording changes and presentation rehearsal.

## When To Enable It

Enable edit mode by default when:

- the user says the deck will be shared with others for review
- the user wants to record a demo showing "生成后还能改"
- the user wants to polish wording during rehearsal
- the deck is a client-facing, course, self-media, or workshop artifact
- the source is a Feishu doc and the user expects document-like editability

Do not enable it by default when:

- the deck is a locked keynote-style presentation
- the deck will be embedded somewhere where a toolbar would distract
- the user wants a clean public landing page with no editing affordance

## How To Add It

When copying a template:

```bash
python3 scripts/copy_template.py <style-slug> /absolute/output/dir --force --editable
```

For an existing generated deck:

```bash
python3 scripts/inject_edit_mode.py /absolute/output/dir/index.html
```

## What Can Be Edited In Browser

Good browser-edit targets:

- titles and subtitles
- paragraphs and bullets
- table cells
- captions
- labels explicitly marked with `data-editable`

Keep these non-editable:

- navigation controls
- buttons
- images and videos
- SVG diagrams and canvas visuals
- script/style code
- complex layout containers

If the user needs to replace an image, remove a video, add a new page, change the interaction model, or redesign a section, treat it as an agent edit to the HTML source instead of a browser edit.

## Suggested User-Facing Explanation

Use this wording when delivering an editable deck:

```text
这份 HTML PPT 已开启可编辑模式。打开页面后按 E 进入编辑模式，直接点文字就能改；按 Cmd+S / Ctrl+S 保存到本机浏览器；点“导出 HTML”可以下载一份带修改内容的新 HTML 文件。图片、视频、版式结构如果要改，继续用对话告诉 Agent 改哪一页。
```

## Video Demo Hook

For competition or self-media demos, show this sequence:

1. Drop a Feishu doc link into the agent.
2. Say one sentence: "把这份文档做成可演示、可编辑的 HTML 网页 PPT。"
3. Open the generated deck and show the visual result.
4. Press `E`, click a headline, change wording live.
5. Press `Cmd+S`, refresh the page, show the edit stayed.
6. Click `导出 HTML`, explain that it becomes a shareable static file.

The message: this is not a frozen screenshot or a normal PPT template. It is a reusable presentation workflow that stays editable after generation.

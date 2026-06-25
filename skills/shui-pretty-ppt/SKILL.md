---
name: shui-pretty-ppt
description: Create polished standalone HTML presentation decks using the Shui Pretty PPT template library. Use when turning notes, scripts, reports, self-media outlines, portfolios, work summaries, academic/business/government/finance-tech materials, product proposals, or Feishu docs into visual web PPT decks. Includes lively creator/personal templates and practical report/presentation templates such as Pastel Blockfolio, Blush Editorial, Mono Curve Slides, One Dot Cinnabar, Ivory Research Deck, Cobalt Executive Deck, Coral Startup Deck, Ribbon Tab Brochure, Sapphire Defense Deck, Vermilion Civic Deck, Blue Growth Deck, and Garden Pop Landing.
---

# Shui Pretty PPT

Use this skill to build **standalone HTML web PPT decks** from a fixed library of reusable visual templates. The output is usually a local static folder containing `index.html` and any required assets. It can be opened directly in a browser, shared as a static page, or used as the visual basis for a talk.

The skill contains twelve templates:

- **Pastel Blockfolio**（粉彩拼贴志）
- **Blush Editorial**（暖粉编辑志）
- **Mono Curve Slides**（墨线白稿）
- **One Dot Cinnabar**（一点丹红）
- **Ivory Research Deck**（象牙研稿）
- **Cobalt Executive Deck**（钴蓝商策）
- **Coral Startup Deck**（珊瑚企简）
- **Ribbon Tab Brochure**（彩签页报）
- **Sapphire Defense Deck**（宝蓝答辩稿）
- **Vermilion Civic Deck**（红色汇报稿）
- **Blue Growth Deck**（蓝色增长稿）
- **Garden Pop Landing**（花园跳色长页）

## What This Skill Does

This is not a generic webpage generator. It turns source material into a **presentation experience**:

1. Pick a template by scenario and visual language.
2. Copy the template instead of writing the PPT from scratch.
3. Convert the user's content into cover, agenda, chapter, data, image, comparison, process, summary, and closing pages.
4. Preserve the chosen template's color system, typography, navigation, interaction model, and motion rules.
5. Verify the resulting deck visually and structurally before delivery.

## Template Modules

Read `references/ppt-template-catalog.md` for the full catalog before choosing a template.

### Module A · Creator, Personal Brand, Portfolio

Use this module when the user wants something more memorable, colorful, editorial, or suitable for self-media sharing, personal showcase, course/product promotion, creator portfolios, and public-facing content.

- **Pastel Blockfolio**（粉彩拼贴志）: energetic tutorials, case studies, workflow recaps, visual explainers.
- **Blush Editorial**（暖粉编辑志）: refined editorial pages, recommendation lists, brand content, catalogs.
- **Mono Curve Slides**（墨线白稿）: clean slide-gallery stories, video lesson pages, lightweight product updates.
- **Ribbon Tab Brochure**（彩签页报）: brochure-like project pages, external proposals, service packages.
- **Blue Growth Deck**（蓝色增长稿）: AI products, growth recaps, creator product launches, friendly business decks.
- **Garden Pop Landing**（花园跳色长页）: self-media tutorials, course launches, creator products, high-energy landing decks.

### Module B · Practical Reports, Government, Workplace, Product Talks

Use this module when the user needs a more practical deck for administrative work, government-adjacent reports, workplace presentations, research summaries, formal briefings, business proposals, thesis defenses, or product roadshows.

- **One Dot Cinnabar**（一点丹红）: formal work reports, executive briefings, proposals, project reviews.
- **Ivory Research Deck**（象牙研稿）: academic talks, research-heavy reports, serious workplace briefings.
- **Cobalt Executive Deck**（钴蓝商策）: business reports, company profiles, product portfolios, partnership proposals.
- **Coral Startup Deck**（珊瑚企简）: warm company decks, team roadshows, project summaries, implementation plans.
- **Sapphire Defense Deck**（宝蓝答辩稿）: thesis defenses, academic presentations, methodology explainers.
- **Vermilion Civic Deck**（红色汇报稿）: civic, administrative, party-building, public-service, and formal leadership-facing reports.

## Workflow

### Step 1 · Intake

If the user already provides a clear outline, source material, and preferred style, start directly.

If the user only gives a topic or rough idea, ask at most three high-impact questions:

1. Who is the audience and sharing scene?
2. Which module is closer: creator/personal showcase or practical report/workplace presentation?
3. Do they have images, screenshots, charts, old slides, or Feishu/Markdown source material?

Use reasonable assumptions when missing details do not block progress.

### Step 2 · Pick A Template

Open `references/ppt-template-catalog.md`, then choose one template by scenario. If the user names a template, use it.

Detailed style references:

- `references/pastel-blockfolio.md`
- `references/blush-editorial.md`
- `references/mono-curve-slides.md`
- `references/one-dot-cinnabar.md`
- `references/ivory-research-deck.md`
- `references/cobalt-executive-deck.md`
- `references/coral-startup-deck.md`
- `references/ribbon-tab-brochure.md`
- `references/sapphire-defense-deck.md`
- `references/vermilion-civic-deck.md`
- `references/blue-growth-deck.md`
- `references/garden-pop-landing.md`

Read the chosen reference before editing the deck.

### Step 3 · Copy The Template

Start from the template instead of hand-building a new PPT shell:

```bash
python3 scripts/copy_template.py <style-slug> /absolute/output/dir
```

Example:

```bash
python3 scripts/copy_template.py cobalt-executive-deck /tmp/shui-cobalt-demo --force
open /tmp/shui-cobalt-demo/index.html
```

Valid slugs:

```text
pastel-blockfolio
blush-editorial
mono-curve-slides
one-dot-cinnabar
ivory-research-deck
cobalt-executive-deck
coral-startup-deck
ribbon-tab-brochure
sapphire-defense-deck
vermilion-civic-deck
blue-growth-deck
garden-pop-landing
```

### Step 4 · Build The Deck

Replace the template content with the user's actual content.

Follow these rules:

- Keep one visual template per deck. Do not mix CSS grammars from multiple templates.
- Preserve the template's color system unless the user explicitly asks for a new style.
- Use the template's existing navigation, page markers, interactions, and motion system.
- Convert long prose into presentation pages: cover, agenda, chapter, key point, data, process, comparison, example, summary, closing.
- Images and videos should live next to `index.html` under a local `assets/` or `images/` folder unless the template already defines another path.
- Do not reuse borrowed web images unless the user owns them, provides them, or explicitly approves the source.

### Step 5 · Verify

Before delivery, check:

- `index.html` exists in the copied output.
- No missing local image/video references.
- No obvious placeholder title or placeholder body text remains.
- The deck opens in a browser.
- Desktop and mobile layouts do not have severe overflow.
- Text does not overlap navigation controls.
- The chosen style still looks distinct and did not collapse into a generic card page.

Useful commands:

```bash
rg "\\[必填\\]|TODO|Lorem|placeholder" /absolute/output/dir
python3 scripts/copy_template.py <style-slug> /tmp/<style-slug>-test --force
```

### Step 6 · Delivery

Return:

- local deck path
- selected template name
- what content was transformed
- any assets that still need the user's replacement
- any verification command results

If publishing, package only the final static deck directory and required assets.

## Naming Rule

The skill/product name is **Shui Pretty PPT**. Individual template names should be public-facing and based on visual language, not the user's name.

Good:

- `Pastel Blockfolio`
- `Cobalt Executive Deck`
- `Vermilion Civic Deck`

Avoid:

- `小水模板 01`
- `小水风格 PPT`

## Growing The Library

When a new PPT result should become a reusable template:

1. Give it an English name, a Chinese name, and a slug.
2. Add the template under `assets/templates/<style-slug>/`.
3. Add a reference file under `references/<style-slug>.md`.
4. Update `references/ppt-template-catalog.md`.
5. Run:
   ```bash
   python3 scripts/copy_template.py <style-slug> /tmp/<style-slug>-test --force
   ```
6. Open the copied `index.html` and verify it visually.

Keep each template distinct. Do not let all styles collapse into the same pastel/card look.

#!/usr/bin/env python3
"""Inject Shui Pretty PPT browser edit mode into an HTML deck."""

from __future__ import annotations

import argparse
from pathlib import Path


START = "<!-- SHUI_PRETTY_PPT_EDIT_MODE_START -->"
END = "<!-- SHUI_PRETTY_PPT_EDIT_MODE_END -->"


SNIPPET = r'''
<!-- SHUI_PRETTY_PPT_EDIT_MODE_START -->
<style id="shui-pretty-ppt-edit-style">
  .shui-edit-toolbar {
    position: fixed;
    z-index: 2147483647;
    top: 14px;
    right: 14px;
    display: flex;
    gap: 6px;
    padding: 6px;
    border: 1px solid rgba(17, 24, 39, 0.16);
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(12px);
    font: 12px/1.2 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    color: #111827;
  }
  .shui-edit-toolbar button {
    appearance: none;
    border: 1px solid rgba(17, 24, 39, 0.18);
    background: #fff;
    color: #111827;
    padding: 6px 8px;
    border-radius: 4px;
    cursor: pointer;
  }
  .shui-edit-toolbar button:hover { background: #f3f4f6; }
  .shui-editing [contenteditable="true"] {
    outline: 1.5px dashed rgba(37, 99, 235, 0.72);
    outline-offset: 3px;
    cursor: text;
  }
  .shui-edit-toast {
    position: fixed;
    z-index: 2147483647;
    right: 14px;
    top: 58px;
    padding: 8px 10px;
    border: 1px solid rgba(17, 24, 39, 0.16);
    background: rgba(17, 24, 39, 0.92);
    color: #fff;
    font: 12px/1.2 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    opacity: 0;
    transform: translateY(-4px);
    transition: opacity .18s ease, transform .18s ease;
    pointer-events: none;
  }
  .shui-edit-toast.is-visible { opacity: 1; transform: translateY(0); }
  @media print {
    .shui-edit-toolbar, .shui-edit-toast { display: none !important; }
  }
</style>
<script id="shui-pretty-ppt-edit-script">
(() => {
  const deckKey = "shui-pretty-ppt-edits:" + location.pathname;
  const editableSelector = [
    "h1", "h2", "h3", "h4", "h5", "h6",
    "p", "li", "blockquote", "td", "th", "figcaption",
    "[data-editable]", ".editable"
  ].join(",");
  const blockedSelector = [
    "script", "style", "svg", "canvas", "video", "audio", "img", "source",
    "button", "nav", "[data-no-edit]", ".shui-edit-toolbar"
  ].join(",");

  let editing = false;
  let toastTimer = null;

  function candidates() {
    return [...document.querySelectorAll(editableSelector)]
      .filter((el) => !el.closest(blockedSelector))
      .filter((el) => (el.textContent || "").trim().length > 0);
  }

  function assignIds() {
    candidates().forEach((el, index) => {
      if (!el.dataset.shuiEditId) {
        el.dataset.shuiEditId = "edit-" + index;
      }
    });
  }

  function readStore() {
    try {
      return JSON.parse(localStorage.getItem(deckKey) || "{}");
    } catch {
      return {};
    }
  }

  function writeStore(data) {
    localStorage.setItem(deckKey, JSON.stringify(data));
  }

  function toast(message) {
    let node = document.querySelector(".shui-edit-toast");
    if (!node) {
      node = document.createElement("div");
      node.className = "shui-edit-toast";
      document.body.appendChild(node);
    }
    node.textContent = message;
    node.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => node.classList.remove("is-visible"), 1500);
  }

  function restore() {
    const data = readStore();
    candidates().forEach((el) => {
      const saved = data[el.dataset.shuiEditId];
      if (saved !== undefined) el.innerHTML = saved;
    });
  }

  function save() {
    assignIds();
    const data = {};
    candidates().forEach((el) => {
      data[el.dataset.shuiEditId] = el.innerHTML;
    });
    writeStore(data);
    toast("已保存到本机浏览器");
  }

  function toggleEdit(force) {
    editing = typeof force === "boolean" ? force : !editing;
    document.body.classList.toggle("shui-editing", editing);
    candidates().forEach((el) => {
      if (editing) {
        el.setAttribute("contenteditable", "true");
        el.setAttribute("spellcheck", "false");
      } else {
        el.removeAttribute("contenteditable");
        el.removeAttribute("spellcheck");
      }
    });
    const button = document.querySelector("[data-shui-edit-toggle]");
    if (button) button.textContent = editing ? "退出编辑" : "编辑";
    toast(editing ? "编辑模式已开启" : "编辑模式已关闭");
  }

  function reset() {
    localStorage.removeItem(deckKey);
    toast("已清除本机修改，刷新后恢复模板内容");
  }

  function exportHtml() {
    save();
    const clone = document.documentElement.cloneNode(true);
    clone.querySelectorAll("[contenteditable], [spellcheck]").forEach((el) => {
      el.removeAttribute("contenteditable");
      el.removeAttribute("spellcheck");
    });
    clone.querySelectorAll(".shui-edit-toolbar, .shui-edit-toast").forEach((el) => el.remove());
    clone.querySelector("body")?.classList.remove("shui-editing");
    const html = "<!doctype html>\n" + clone.outerHTML;
    const blob = new Blob([html], { type: "text/html;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = (document.title || "shui-pretty-ppt").replace(/[\\/:*?"<>|]+/g, "-") + "-edited.html";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  function toolbar() {
    if (document.querySelector(".shui-edit-toolbar")) return;
    const bar = document.createElement("div");
    bar.className = "shui-edit-toolbar";
    bar.setAttribute("data-no-edit", "true");
    bar.innerHTML = [
      '<button type="button" data-shui-edit-toggle>编辑</button>',
      '<button type="button" data-shui-edit-save>保存</button>',
      '<button type="button" data-shui-edit-export>导出 HTML</button>',
      '<button type="button" data-shui-edit-reset>重置</button>'
    ].join("");
    document.body.appendChild(bar);
    bar.querySelector("[data-shui-edit-toggle]").addEventListener("click", () => toggleEdit());
    bar.querySelector("[data-shui-edit-save]").addEventListener("click", save);
    bar.querySelector("[data-shui-edit-export]").addEventListener("click", exportHtml);
    bar.querySelector("[data-shui-edit-reset]").addEventListener("click", reset);
  }

  document.addEventListener("keydown", (event) => {
    const key = event.key.toLowerCase();
    if (key === "e" && !event.metaKey && !event.ctrlKey && !event.altKey) {
      const tag = document.activeElement?.tagName?.toLowerCase();
      if (tag !== "input" && tag !== "textarea") toggleEdit();
    }
    if (key === "s" && (event.metaKey || event.ctrlKey)) {
      event.preventDefault();
      save();
    }
  });

  assignIds();
  restore();
  toolbar();
})();
</script>
<!-- SHUI_PRETTY_PPT_EDIT_MODE_END -->
'''


def inject_edit_mode(index_path: Path) -> bool:
    index_path = index_path.expanduser().resolve()
    if not index_path.exists():
        raise FileNotFoundError(f"Missing HTML file: {index_path}")

    html = index_path.read_text(encoding="utf-8", errors="replace")
    if START in html and END in html:
        before, rest = html.split(START, 1)
        _, after = rest.split(END, 1)
        html = before + SNIPPET.strip() + after
    elif "</body>" in html.lower():
        body_at = html.lower().rfind("</body>")
        html = html[:body_at] + SNIPPET + "\n" + html[body_at:]
    else:
        html = html + "\n" + SNIPPET + "\n"

    index_path.write_text(html, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Inject browser edit mode into a Shui Pretty PPT deck.")
    parser.add_argument("html", help="Path to index.html or another HTML file")
    args = parser.parse_args()
    inject_edit_mode(Path(args.html))
    print(Path(args.html).expanduser().resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# Script to build the updated LightStream pitch deck with hand-drawn blueprint aesthetics,
# off-canvas burger drawer, bilingual RU/EN support, and strict sales funnel.
import os
import json

metrics_path = r"D:\lightstream\pitch-site\metrics.json"
with open(metrics_path, "r", encoding="utf-8") as f:
    metrics = json.load(f)

json_str = json.dumps(metrics, ensure_ascii=False)

html_content = r'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>LightStream — 100% Share of Voice B2B Brief & Analytics</title>
  <meta name="description" content="Эксклюзивный B2B-оффер онлайн-кинотеатра LightStream: 100% Share of Voice для одного рекламодателя, верифицированная аналитика 90 дней, сравнение с Netflix, ROI-калькулятор.">
  
  <!-- Fonts: Inter (Sans), JetBrains Mono (Technical/Data), Caveat (Hand-drawn annotations) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">

  <style>
    :root {
      --bg: #09090c;
      --bg-blueprint: #0d0e12;
      --card-bg: #121318;
      --card-border: #23242c;
      --card-hover: #191a22;
      --text: #fdfdfd;
      --text-muted: #a3a3af;
      --text-dim: #717180;
      --sketch-line: #3a3b48;
      --sketch-accent: #ffffff;
      --accent-green: #10b981;
      --accent-blue: #3b82f6;
      --accent-amber: #f59e0b;
      --accent-red: #ef4444;
      
      --sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      --mono: 'JetBrains Mono', monospace;
      --hand: 'Caveat', cursive, sans-serif;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden;
      background-color: var(--bg);
      background-image: 
        radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.05) 1px, transparent 0),
        linear-gradient(to right, rgba(255, 255, 255, 0.015) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(255, 255, 255, 0.015) 1px, transparent 1px);
      background-size: 28px 28px, 56px 56px, 56px 56px;
      color: var(--text);
      font-family: var(--sans);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 80px;
    }

    .container {
      width: 100%;
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 24px;
      box-sizing: border-box;
    }

    /* Hand-drawn sketch badges & callouts */
    .hand-note {
      font-family: var(--hand);
      font-size: 19px;
      color: #f4f4f5;
      line-height: 1.2;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      letter-spacing: 0.02em;
    }

    .hand-badge {
      font-family: var(--hand);
      font-size: 16px;
      padding: 2px 10px;
      border: 1px dashed var(--sketch-line);
      border-radius: 14px 4px 16px 5px;
      color: #e4e4e7;
      background: rgba(255, 255, 255, 0.03);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    /* Sketchy architectural borders */
    .sketch-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      position: relative;
      transition: all 0.2s ease;
      box-shadow: 0 4px 20px rgba(0, 0, 0, 0.35);
    }

    .sketch-card:hover {
      border-color: #3f404d;
      transform: translateY(-2px);
    }

    .sketch-card::before {
      content: '';
      position: absolute;
      top: -1px;
      left: 14px;
      right: 14px;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
      pointer-events: none;
    }

    /* Header & Navigation */
    header {
      position: sticky;
      top: 0;
      z-index: 1000;
      background: rgba(9, 9, 12, 0.94);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      padding: 12px 0;
      width: 100%;
    }

    .nav-row {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
    }

    .logo-link {
      display: flex;
      align-items: center;
      gap: 12px;
      text-decoration: none;
      color: inherit;
      cursor: pointer;
    }

    .logo-mark {
      width: 28px;
      height: 28px;
      background: #fafafa;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #ffffff;
      box-shadow: 0 0 12px rgba(255, 255, 255, 0.25);
    }

    .logo-mark svg {
      width: 14px;
      height: 14px;
      fill: #09090c;
    }

    .logo-name {
      font-size: 17px;
      font-weight: 700;
      letter-spacing: -0.02em;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    /* Language Toggle */
    .lang-toggle {
      display: inline-flex;
      background: #14141a;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 3px;
      gap: 2px;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
    }

    .lang-btn {
      background: transparent;
      border: none;
      color: var(--text-dim);
      padding: 4px 9px;
      border-radius: 5px;
      cursor: pointer;
      transition: all 0.15s ease;
    }

    .lang-btn.active {
      background: #272832;
      color: #fafafa;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.5);
    }

    /* Primary & Secondary Buttons */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      padding: 8px 16px;
      border-radius: 7px;
      font-size: 13px;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
      white-space: nowrap;
      min-height: 38px;
    }

    .btn-secondary {
      background: #15161d;
      border: 1px solid var(--card-border);
      color: var(--text);
    }

    .btn-secondary:hover {
      background: #20212a;
      border-color: #3f404d;
    }

    .btn-primary {
      background: #fafafa;
      color: #09090c;
      font-weight: 600;
      border: 1px solid #ffffff;
      box-shadow: 0 0 16px rgba(255, 255, 255, 0.15);
    }

    .btn-primary:hover {
      background: #e4e4e7;
      transform: translateY(-1px);
    }

    /* Hamburger Menu Button */
    .burger-btn {
      width: 40px;
      height: 40px;
      background: #14141a;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      display: inline-flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 5px;
      cursor: pointer;
      transition: all 0.2s ease;
      padding: 0;
      z-index: 1001;
    }

    .burger-btn:hover {
      background: #1f2029;
      border-color: #525363;
    }

    .burger-btn span {
      width: 20px;
      height: 2px;
      background: #f4f4f5;
      border-radius: 2px;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      transform-origin: center;
    }

    .burger-btn.active span:nth-child(1) {
      transform: translateY(7px) rotate(45deg);
    }

    .burger-btn.active span:nth-child(2) {
      opacity: 0;
      transform: scaleX(0);
    }

    .burger-btn.active span:nth-child(3) {
      transform: translateY(-7px) rotate(-45deg);
    }

    /* Off-Canvas Backdrop & Drawer */
    .drawer-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.7);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      opacity: 0;
      visibility: hidden;
      transition: opacity 0.25s ease, visibility 0.25s ease;
      z-index: 1500;
    }

    .drawer-backdrop.show {
      opacity: 1;
      visibility: visible;
    }

    .drawer-panel {
      position: fixed;
      top: 0;
      right: 0;
      bottom: 0;
      width: 380px;
      max-width: calc(100vw - 24px);
      background: #101015;
      border-left: 1px solid #2e2f3a;
      box-shadow: -10px 0 40px rgba(0, 0, 0, 0.85);
      z-index: 1600;
      transform: translateX(100%);
      transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      box-sizing: border-box;
      overflow-y: auto;
    }

    .drawer-panel.show {
      transform: translateX(0);
    }

    .drawer-header {
      padding: 20px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #20212b;
    }

    .drawer-title {
      font-size: 15px;
      font-weight: 700;
      font-family: var(--mono);
      letter-spacing: -0.01em;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .drawer-close {
      background: #1a1b24;
      border: 1px solid #2e2f3a;
      color: #fafafa;
      width: 32px;
      height: 32px;
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 16px;
      transition: all 0.15s ease;
    }

    .drawer-close:hover {
      background: #272836;
      border-color: #525363;
    }

    .drawer-nav {
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      gap: 4px;
      flex-grow: 1;
    }

    .drawer-category {
      font-family: var(--mono);
      font-size: 10px;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      padding: 12px 10px 4px;
    }

    .drawer-link {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 12px;
      border-radius: 8px;
      text-decoration: none;
      color: var(--text-muted);
      font-size: 13.5px;
      font-weight: 500;
      transition: all 0.12s ease;
    }

    .drawer-link:hover {
      background: #191a24;
      color: #fafafa;
    }

    .drawer-link span {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .drawer-link .num {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
      width: 18px;
    }

    .drawer-link .tag {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--text-dim);
      padding: 2px 6px;
      background: #171821;
      border-radius: 4px;
      border: 1px solid #262733;
    }

    .drawer-footer {
      padding: 20px 24px;
      border-top: 1px solid #20212b;
      display: flex;
      flex-direction: column;
      gap: 10px;
      background: #0d0d12;
    }

    /* Hero Section */
    .hero {
      padding: 56px 0 44px;
      position: relative;
    }

    .hero-top-bar {
      display: flex;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      margin-bottom: 24px;
    }

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 4px 12px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-muted);
    }

    .audience-switcher {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 6px;
      background: #101117;
      border: 1px solid var(--card-border);
      border-radius: 30px;
    }

    .aud-label {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
      padding: 0 6px 0 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .aud-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: transparent;
      border: none;
      color: var(--text-muted);
      font-family: var(--sans);
      font-size: 12px;
      font-weight: 500;
      padding: 5px 12px;
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .aud-btn:hover {
      color: var(--text);
    }

    .aud-btn.active {
      background: #252632;
      color: #fafafa;
      font-weight: 600;
      box-shadow: 0 1px 6px rgba(0,0,0,0.4);
    }

    .pulse-dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent-green);
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.8);
      flex-shrink: 0;
    }

    h1 {
      font-size: clamp(26px, 4.5vw, 44px);
      font-weight: 700;
      line-height: 1.22;
      letter-spacing: -0.03em;
      margin-bottom: 20px;
      max-width: 980px;
      position: relative;
    }

    .hero-sub {
      font-size: clamp(15px, 2.2vw, 17.5px);
      color: var(--text-muted);
      line-height: 1.62;
      max-width: 880px;
      margin-bottom: 28px;
    }

    .hero-sub strong {
      color: var(--text);
    }

    /* Hero Annotation Callout */
    .hero-callout-row {
      display: flex;
      align-items: center;
      gap: 20px;
      margin-bottom: 32px;
      flex-wrap: wrap;
    }

    .sketch-arrow-wrap {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-family: var(--hand);
      font-size: 21px;
      color: #fafafa;
    }

    .sketch-arrow-wrap svg {
      width: 44px;
      height: 22px;
      stroke: #fafafa;
      stroke-width: 2;
      fill: none;
    }

    /* Hero CTA Row */
    .hero-cta-group {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
      margin-bottom: 36px;
    }

    /* Blueprint Meta Specs Grid */
    .blueprint-specs {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      padding: 18px 20px;
      background: #0f1016;
      border: 1px dashed var(--sketch-line);
      border-radius: 10px;
      font-family: var(--mono);
      font-size: 12px;
    }

    .spec-item {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .spec-label {
      color: var(--text-dim);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }

    .spec-val {
      color: var(--text);
      font-weight: 600;
      word-break: break-all;
    }

    /* Section Styles */
    .section {
      padding: 64px 0 32px;
      position: relative;
    }

    .section-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 28px;
      flex-wrap: wrap;
      gap: 16px;
    }

    .section-title {
      font-size: clamp(22px, 3.2vw, 28px);
      font-weight: 700;
      letter-spacing: -0.025em;
      margin-bottom: 6px;
    }

    .section-desc {
      font-size: 14.5px;
      color: var(--text-muted);
      max-width: 760px;
      line-height: 1.55;
    }

    /* KPI Cards (Handcrafted sketch style) */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 24px;
    }

    .kpi-card {
      padding: 22px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .kpi-head {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }

    .kpi-label {
      font-family: var(--mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
    }

    .kpi-num {
      font-family: var(--mono);
      font-size: clamp(26px, 3.5vw, 34px);
      font-weight: 700;
      letter-spacing: -0.03em;
      color: var(--text);
      margin-bottom: 6px;
    }

    .kpi-note {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.45;
    }

    .kpi-hand-badge {
      font-family: var(--hand);
      font-size: 16px;
      color: #f4f4f5;
      margin-top: 10px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    /* Stage Tabs */
    .stage-switch {
      display: inline-flex;
      background: #12131a;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 3px;
      gap: 3px;
    }

    .stage-tab {
      background: transparent;
      border: none;
      color: var(--text-dim);
      font-family: var(--mono);
      font-size: 11.5px;
      padding: 6px 14px;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }

    .stage-tab.active {
      background: #252632;
      color: #fafafa;
      font-weight: 600;
    }

    /* Handcrafted Dual Infographics Grid */
    .infographics-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }

    .chart-card {
      padding: 24px;
    }

    .chart-card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      gap: 12px;
      flex-wrap: wrap;
    }

    .chart-card-title {
      font-size: 16px;
      font-weight: 600;
      letter-spacing: -0.01em;
    }

    .chart-card-sub {
      font-size: 12px;
      color: var(--text-dim);
      margin-top: 2px;
    }

    /* SVG Traffic Chart (Hand-drawn Blueprint feel) */
    .svg-traffic-wrap {
      width: 100%;
      height: 220px;
      position: relative;
    }

    .svg-traffic-wrap svg {
      width: 100%;
      height: 100%;
      display: block;
    }

    .chart-footer-stats {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 20px;
      padding-top: 16px;
      border-top: 1px dashed var(--sketch-line);
    }

    .c-stat-k {
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--text-dim);
      text-transform: uppercase;
    }

    .c-stat-v {
      font-family: var(--mono);
      font-size: 17px;
      font-weight: 700;
      color: #fafafa;
      margin-top: 2px;
    }

    /* Radar Chart Container */
    .radar-svg-box {
      width: 100%;
      height: 240px;
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .radar-legend {
      display: flex;
      justify-content: center;
      gap: 20px;
      font-family: var(--mono);
      font-size: 12px;
      margin-top: 14px;
      flex-wrap: wrap;
    }

    .legend-tag {
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .legend-color-box {
      width: 10px;
      height: 10px;
      border-radius: 2px;
    }

    /* Device & GEO Split */
    .devices-geo-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }

    .progress-list {
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .progress-row {
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .progress-labels {
      display: flex;
      justify-content: space-between;
      font-size: 12.5px;
    }

    .progress-labels span:first-child {
      font-weight: 500;
      color: #fafafa;
    }

    .progress-labels span:last-child {
      font-family: var(--mono);
      font-weight: 600;
      color: var(--text-muted);
    }

    .progress-track {
      height: 7px;
      background: #1c1d26;
      border-radius: 4px;
      overflow: hidden;
      border: 1px solid rgba(255, 255, 255, 0.05);
    }

    .progress-fill {
      height: 100%;
      background: #fafafa;
      border-radius: 4px;
      transition: width 0.5s ease;
    }

    /* Interactive & Intuitive Heatmap Matrix */
    .heat-card {
      padding: 24px;
      margin-bottom: 24px;
    }

    .heat-toolbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin-top: 14px;
      margin-bottom: 16px;
      flex-wrap: wrap;
    }

    .heat-presets {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }

    .heat-preset-btn {
      font-family: var(--mono);
      font-size: 11px;
      padding: 6px 12px;
      border: 1px solid var(--border-subtle);
      background: rgba(255, 255, 255, 0.03);
      color: var(--text-muted);
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.2s ease;
    }

    .heat-preset-btn:hover {
      border-color: #717180;
      color: #fafafa;
    }

    .heat-preset-btn.active {
      background: rgba(255, 255, 255, 0.12);
      border-color: #fafafa;
      color: #fafafa;
      font-weight: 600;
    }

    .heat-legend {
      display: flex;
      align-items: center;
      gap: 6px;
      font-family: var(--mono);
      font-size: 10.5px;
      color: var(--text-dim);
    }

    .heat-legend-dots {
      display: flex;
      gap: 3px;
    }

    .heat-dot {
      width: 10px;
      height: 10px;
      border-radius: 2px;
    }

    .heat-main-grid {
      display: grid;
      grid-template-columns: 1.6fr 1fr;
      gap: 20px;
      align-items: stretch;
    }

    @media (max-width: 992px) {
      .heat-main-grid {
        grid-template-columns: 1fr;
      }
    }

    /* Heatmap Table */
    .heat-table-wrap {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 16px;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }

    .heat-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 4px;
      font-family: var(--mono);
      min-width: 520px;
    }

    .heat-th {
      font-size: 10px;
      color: var(--text-dim);
      font-weight: 500;
      text-align: center;
      padding: 4px;
    }

    .heat-th.prime {
      color: #fafafa;
      font-weight: 700;
    }

    .heat-day-lbl {
      font-size: 11px;
      font-weight: 600;
      color: var(--text-muted);
      padding-right: 8px;
      white-space: nowrap;
    }

    .heat-day-lbl.record {
      color: #fafafa;
    }

    .heat-cell {
      height: 26px;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }

    .heat-cell:hover {
      transform: scale(1.15);
      z-index: 10;
      outline: 2px solid #ffffff;
      outline-offset: 1px;
    }

    .heat-cell.is-selected {
      outline: 2px solid var(--accent-green);
      outline-offset: 2px;
      transform: scale(1.1);
      z-index: 9;
    }

    /* Intensity levels */
    .heat-lvl-1 { background: #181923; }
    .heat-lvl-2 { background: #272836; }
    .heat-lvl-3 { background: #3f4258; }
    .heat-lvl-4 { background: #686c8c; }
    .heat-lvl-5 {
      background: #fafafa;
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
    }

    /* Live Telemetry Inspector Card */
    .heat-inspector {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 18px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .insp-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
    }

    .insp-slot-title {
      font-size: 15px;
      font-weight: 700;
      color: #fafafa;
      margin-bottom: 4px;
    }

    .insp-slot-status {
      font-size: 11px;
      font-family: var(--mono);
      color: var(--accent-green);
    }

    .insp-gauge-wrap {
      margin-bottom: 16px;
    }

    .insp-gauge-head {
      display: flex;
      justify-content: space-between;
      font-size: 11px;
      font-family: var(--mono);
      color: var(--text-dim);
      margin-bottom: 5px;
    }

    .insp-gauge-track {
      width: 100%;
      height: 7px;
      background: #191a26;
      border-radius: 4px;
      overflow: hidden;
    }

    .insp-gauge-fill {
      height: 100%;
      background: #fafafa;
      border-radius: 4px;
      box-shadow: 0 0 8px rgba(255, 255, 255, 0.4);
      transition: width 0.3s ease;
    }

    .insp-metrics-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 10px;
      margin-bottom: 14px;
    }

    .insp-m-item {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid rgba(255, 255, 255, 0.05);
      border-radius: 4px;
      padding: 8px 10px;
    }

    .insp-m-k {
      font-size: 10px;
      font-family: var(--mono);
      color: var(--text-dim);
      text-transform: uppercase;
      margin-bottom: 3px;
    }

    .insp-m-v {
      font-size: 13.5px;
      font-weight: 700;
      color: var(--text-main);
    }

    .insp-tip {
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.4;
      border-top: 1px dashed var(--border-subtle);
      padding-top: 10px;
    }

    /* 3 Bottom Takeaway Cards */
    .heat-takeaways {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 12px;
      margin-top: 18px;
    }

    @media (max-width: 768px) {
      .heat-takeaways {
        grid-template-columns: 1fr;
      }
    }

    .heat-takeaway-card {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 14px;
    }

    .heat-takeaway-tag {
      font-size: 10px;
      font-family: var(--mono);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      margin-bottom: 4px;
      display: block;
    }

    .heat-takeaway-val {
      font-size: 14px;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 4px;
    }

    .heat-takeaway-desc {
      font-size: 11px;
      color: var(--text-muted);
      line-height: 1.45;
    }

    /* ROI Calculator */
    .calc-box {
      padding: 26px;
      margin-bottom: 28px;
    }

    .calc-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }

    .calc-slider-wrap label {
      display: flex;
      justify-content: space-between;
      font-family: var(--mono);
      font-size: 12px;
      color: var(--text-dim);
      margin-bottom: 10px;
    }

    .calc-slider-wrap label strong {
      color: #fafafa;
      font-size: 14px;
    }

    .calc-slider {
      width: 100%;
      height: 8px;
      background: #252632;
      border-radius: 4px;
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }

    .calc-slider::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #fafafa;
      border: 2px solid #09090c;
      box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
    }

    .calc-results-row {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      background: #0b0b0f;
      border: 1px dashed var(--sketch-line);
      border-radius: 10px;
      padding: 20px;
    }

    .res-item {
      display: flex;
      flex-direction: column;
    }

    .res-lbl {
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
      margin-bottom: 4px;
    }

    .res-val {
      font-family: var(--mono);
      font-size: clamp(18px, 2.5vw, 22px);
      font-weight: 700;
      color: #fafafa;
    }

    .res-sub {
      font-size: 11px;
      color: var(--text-muted);
    }

    /* Comparison Matrix */
    .matrix-box {
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      padding: 16px;
      margin-bottom: 24px;
    }

    .matrix-tbl {
      width: 100%;
      min-width: 680px;
      border-collapse: collapse;
      font-size: 13px;
    }

    .matrix-tbl th, .matrix-tbl td {
      padding: 14px 16px;
      border-bottom: 1px solid #1f202b;
    }

    .matrix-tbl th {
      font-family: var(--mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
      background: #14151d;
    }

    .matrix-tbl tr:last-child td {
      border-bottom: none;
    }

    .tag-yes {
      background: #064e3b;
      color: #34d399;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
    }

    .tag-soon {
      background: #252632;
      color: #e4e4e7;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
      border: 1px solid #3f404d;
    }

    .tag-partial {
      background: #422006;
      color: #fbbf24;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
    }

    .tag-no {
      background: #1c1917;
      color: #78716c;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      padding: 2px 7px;
      border-radius: 4px;
    }

    /* ==========================================================================
       STEP 3: THE MOAT & UNIT ECONOMICS STYLES
       ========================================================================== */
    .moat-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 20px;
      margin-top: 24px;
    }
    @media (max-width: 860px) {
      .moat-grid {
        grid-template-columns: 1fr;
      }
    }

    .moat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 10px;
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: border-color 0.2s, transform 0.2s;
    }
    .moat-card:hover {
      border-color: #4a4b5d;
      transform: translateY(-2px);
    }

    .moat-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .moat-badge {
      font-family: var(--mono);
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 4px;
      background: #1b1c28;
      border: 1px solid #2f3042;
      color: #93c5fd;
    }

    .moat-title {
      font-size: 17px;
      font-weight: 700;
      color: #ffffff;
      letter-spacing: -0.01em;
    }

    .moat-desc {
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .moat-box-comp {
      background: #0d0e15;
      border: 1px solid #1e1f2b;
      border-radius: 6px;
      padding: 10px 14px;
      margin-top: auto;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }

    .moat-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 11px;
      padding: 3px 0;
      border-bottom: 1px dashed #1a1b26;
    }
    .moat-row:last-child {
      border-bottom: none;
    }

    .moat-lbl {
      color: var(--text-dim);
      font-family: var(--mono);
    }
    .moat-val-bad {
      color: #f87171;
      font-family: var(--mono);
    }
    .moat-val-good {
      color: #34d399;
      font-family: var(--mono);
      font-weight: 700;
    }

    /* ==========================================================================
       STEP 4: SHIPPING VELOCITY CHANGELOG STYLES
       ========================================================================== */
    .velocity-box {
      background: #090a10;
      border: 1px solid #222332;
      border-radius: 10px;
      overflow: hidden;
      margin-top: 24px;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5);
    }

    .velocity-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 12px 18px;
      background: #12131d;
      border-bottom: 1px solid #1f202b;
      font-family: var(--mono);
      font-size: 12px;
    }

    .velocity-header-title {
      display: flex;
      align-items: center;
      gap: 10px;
      color: #fafafa;
      font-weight: 600;
    }

    .velocity-branch {
      background: #1c1d29;
      padding: 2px 7px;
      border-radius: 4px;
      color: #a1a1aa;
      font-size: 11px;
      border: 1px solid #2e2f40;
    }

    .velocity-list {
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .velocity-item {
      display: flex;
      align-items: flex-start;
      gap: 14px;
      padding-bottom: 14px;
      border-bottom: 1px solid #181924;
    }
    .velocity-item:last-child {
      border-bottom: none;
      padding-bottom: 0;
    }

    .v-tag {
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      background: rgba(96, 165, 250, 0.12);
      color: #60a5fa;
      border: 1px solid rgba(96, 165, 250, 0.3);
      padding: 2px 8px;
      border-radius: 4px;
      white-space: nowrap;
    }

    .v-body {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .v-meta {
      display: flex;
      align-items: center;
      gap: 10px;
      font-family: var(--mono);
      font-size: 11px;
    }

    .v-title {
      color: #ffffff;
      font-weight: 600;
      font-size: 13px;
    }

    .v-commit {
      color: var(--text-dim);
    }

    .v-desc {
      color: var(--text-muted);
      font-size: 12px;
      line-height: 1.5;
    }

    .velocity-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 18px;
      background: #0d0e16;
      border-top: 1px solid #1a1b26;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-dim);
    }

    /* ==========================================================================
       STEP 5: ONE-CLICK EXECUTIVE MEMO EXPORT
       ========================================================================== */
    .memo-bar {
      margin-top: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: linear-gradient(90deg, #12131d 0%, #171825 100%);
      border: 1px dashed #3a3b4e;
      border-radius: 8px;
      padding: 14px 20px;
      gap: 16px;
      flex-wrap: wrap;
    }

    .memo-info {
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .memo-title {
      color: #ffffff;
      font-weight: 700;
      font-size: 13px;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .memo-sub {
      color: var(--text-muted);
      font-size: 12px;
    }

    .memo-btn {
      background: #ffffff;
      color: #000000;
      font-family: var(--mono);
      font-weight: 700;
      font-size: 12px;
      border: none;
      border-radius: 6px;
      padding: 9px 18px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      box-shadow: 0 4px 14px rgba(255, 255, 255, 0.15);
      white-space: nowrap;
    }
    .memo-btn:hover {
      background: #f0f0f5;
      transform: translateY(-1px);
      box-shadow: 0 6px 20px rgba(255, 255, 255, 0.25);
    }
    .memo-btn:active {
      transform: translateY(0);
    }

    /* Toast Notification */
    .toast-memo {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #11121b;
      border: 1px solid #10b981;
      color: #34d399;
      padding: 12px 20px;
      border-radius: 8px;
      font-family: var(--mono);
      font-size: 12px;
      box-shadow: 0 12px 35px rgba(0, 0, 0, 0.8), 0 0 15px rgba(16, 185, 129, 0.2);
      z-index: 9999;
      opacity: 0;
      transform: translateY(16px);
      transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      pointer-events: none;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .toast-memo.show {
      opacity: 1;
      transform: translateY(0);
    }

    /* ==========================================================================
       FEATURE TIMELINE ARROW (Strict Hand-Drawn Blueprint Vertical Arrow)
       ========================================================================== */
    .timeline-wrap {
      position: relative;
      max-width: 960px;
      margin: 40px auto 20px;
      padding: 20px 0 60px;
      width: 100%;
    }

    .timeline-stem {
      position: absolute;
      top: 0;
      bottom: 24px;
      left: 50%;
      width: 4px;
      background: linear-gradient(180deg, #3a3b48 0%, #717180 50%, #ffffff 100%);
      transform: translateX(-50%);
      border-radius: 2px;
    }

    .timeline-stem::after {
      content: '';
      position: absolute;
      bottom: -18px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 11px solid transparent;
      border-right: 11px solid transparent;
      border-top: 18px solid #ffffff;
      filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.8));
    }

    .timeline-row {
      position: relative;
      margin-bottom: 34px;
      width: 50%;
      display: flex;
      align-items: center;
      box-sizing: border-box;
    }

    .timeline-row.left {
      left: 0;
      padding-right: 54px;
      justify-content: flex-end;
    }

    .timeline-row.right {
      left: 50%;
      padding-left: 54px;
      justify-content: flex-start;
    }

    .timeline-circle {
      position: absolute;
      top: 50%;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: #101117;
      border: 3px solid #717180;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
      font-family: var(--mono);
      color: #fafafa;
      transform: translateY(-50%);
      z-index: 5;
      box-shadow: 0 0 0 4px #09090c;
    }

    .timeline-row.left .timeline-circle {
      right: -18px;
    }

    .timeline-row.right .timeline-circle {
      left: -18px;
    }

    .timeline-connector {
      position: absolute;
      top: 50%;
      height: 2px;
      border-top: 2px dashed #525363;
      width: 38px;
      z-index: 1;
    }

    .timeline-row.left .timeline-connector {
      right: 18px;
    }

    .timeline-row.right .timeline-connector {
      left: 18px;
    }

    .node-done {
      border-color: #10b981;
      background: #064e3b;
      box-shadow: 0 0 12px rgba(16, 185, 129, 0.5), 0 0 0 4px #09090c;
    }

    .node-wip {
      border-color: #3b82f6;
      background: #1e3a8a;
      box-shadow: 0 0 12px rgba(59, 130, 246, 0.5), 0 0 0 4px #09090c;
    }

    .node-plan {
      border-color: #e4e4e7;
      background: #252632;
      box-shadow: 0 0 10px rgba(228, 228, 231, 0.3), 0 0 0 4px #09090c;
    }

    .t-card {
      padding: 16px 20px;
      width: 100%;
      max-width: 400px;
    }

    .t-card-head {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      gap: 8px;
    }

    .t-badge.done {
      background: #064e3b;
      color: #34d399;
    }
    .t-badge.wip {
      background: #1e3a8a;
      color: #60a5fa;
    }
    .t-badge.plan {
      background: #252632;
      color: #e4e4e7;
    }

    .t-stage {
      font-family: var(--mono);
      font-size: 10px;
      color: var(--text-dim);
    }

    .t-title {
      font-size: 14.5px;
      font-weight: 600;
      margin-bottom: 4px;
      color: #fafafa;
    }

    .t-desc {
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
    }

    .timeline-grand {
      max-width: 580px;
      margin: 40px auto 0;
      text-align: center;
      position: relative;
      z-index: 10;
    }

    .grand-card {
      padding: 22px;
      border: 1px solid #525363;
      background: #13141c;
      box-shadow: 0 0 30px rgba(255, 255, 255, 0.06);
    }

    /* Deal Options */
    .deals-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }

    .deal-card {
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }

    .deal-card.primary {
      border-color: #525363;
      box-shadow: 0 0 24px rgba(255, 255, 255, 0.05);
    }

    .deal-badge {
      font-family: var(--mono);
      font-size: 10px;
      padding: 3px 7px;
      background: #252632;
      border-radius: 4px;
      color: #fafafa;
      display: inline-block;
      margin-bottom: 12px;
      align-self: flex-start;
    }

    .deal-title {
      font-size: 17px;
      font-weight: 700;
      margin-bottom: 6px;
    }

    .deal-sub {
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 18px;
      line-height: 1.45;
    }

    .deal-pts {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 24px;
      flex-grow: 1;
    }

    .deal-pts li {
      padding-left: 14px;
      position: relative;
    }

    .deal-pts li::before {
      content: '•';
      position: absolute;
      left: 0;
      color: var(--text-dim);
    }

    .deal-footer {
      font-size: 11px;
      color: var(--text-dim);
      border-top: 1px dashed var(--sketch-line);
      padding-top: 12px;
    }

    /* Bottom Direct Conversion Box */
    .cta-banner {
      margin-top: 56px;
      padding: 36px 32px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 24px;
      flex-wrap: wrap;
      background: #12131a;
      border: 1px solid #3f404d;
    }

    .cta-left {
      max-width: 620px;
      flex: 1 1 300px;
    }

    .cta-title {
      font-size: clamp(20px, 3vw, 25px);
      font-weight: 700;
      margin-bottom: 8px;
    }

    .cta-desc {
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.55;
    }

    .cta-btns {
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex-shrink: 0;
    }

    /* Footer */
    footer {
      margin-top: 56px;
      padding: 32px 0 64px;
      border-top: 1px solid #1f202b;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-family: var(--mono);
      font-size: 12px;
      color: var(--text-dim);
      flex-wrap: wrap;
      gap: 12px;
    }

    /* Responsive Breakpoints */
    @media (max-width: 992px) {
      .infographics-grid, .devices-geo-grid {
        grid-template-columns: 1fr;
      }
      .deals-grid {
        grid-template-columns: 1fr;
      }
      .blueprint-specs {
        grid-template-columns: repeat(2, 1fr);
      }
      .kpi-grid {
        grid-template-columns: repeat(2, 1fr);
      }
      .calc-grid {
        grid-template-columns: 1fr;
      }
      .calc-results-row {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    /* Mobile Timeline Adaptation */
    @media (max-width: 768px) {
      .timeline-wrap {
        padding: 10px 0 36px;
        margin: 20px auto;
      }
      .timeline-stem {
        left: 20px;
        transform: none;
      }
      .timeline-row {
        width: 100%;
        left: 0 !important;
        padding-left: 54px !important;
        padding-right: 0 !important;
        justify-content: flex-start !important;
      }
      .timeline-circle {
        left: 2px !important;
        right: auto !important;
      }
      .timeline-connector {
        left: 20px !important;
        right: auto !important;
        width: 34px;
      }
      .t-card {
        max-width: 100%;
      }
      .timeline-grand {
        padding-left: 54px;
        text-align: left;
      }
    }

    @media (max-width: 640px) {
      .container {
        padding: 0 16px;
      }
      .header-actions-desktop {
        display: none;
      }
      .blueprint-specs {
        grid-template-columns: 1fr;
      }
      .kpi-grid {
        grid-template-columns: 1fr;
      }
      .calc-results-row {
        grid-template-columns: 1fr;
      }
      .chart-footer-stats {
        grid-template-columns: repeat(2, 1fr);
      }
      .cta-banner {
        padding: 24px 20px;
      }
      .cta-btns {
        width: 100%;
      }
      .cta-btns .btn {
        width: 100%;
      }
      footer {
        flex-direction: column;
        align-items: flex-start;
      }
    }
  </style>
</head>
<body id="top">

  <!-- Sticky Top Header -->
  <header>
    <div class="container nav-row">
      <!-- Logo left -> Leads to the very top (#top) as requested -->
      <a href="#top" class="logo-link" title="LightStream — Наверх">
        <div class="logo-mark">
          <svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
        </div>
        <div>
          <span class="logo-name">LightStream</span>
          <span class="hand-badge" style="margin-left:6px; font-size:14px;">100% SoV</span>
        </div>
      </a>

      <!-- Header Right Actions -->
      <div class="nav-actions">
        <!-- Language Switcher RU | EN -->
        <div class="lang-toggle" role="group" aria-label="Language selection">
          <button class="lang-btn active" id="btnLangRu" onclick="setLang('ru')">RU</button>
          <button class="lang-btn" id="btnLangEn" onclick="setLang('en')">EN</button>
        </div>

        <!-- Open App Button -> Leads to https://lightstream.ws as requested -->
        <a href="https://lightstream.ws" target="_blank" rel="noopener" class="btn btn-secondary header-actions-desktop" id="headBtnOpenApp">
          <span data-i18n="head_open_app">Кинотеатр ↗</span>
        </a>

        <!-- TG Contact -->
        <a href="https://t.me/shitmane" target="_blank" rel="noopener" class="btn btn-primary header-actions-desktop" id="headBtnTg">
          <span data-i18n="head_contact_tg">Связаться в TG</span>
        </a>

        <!-- Hamburger Button -->
        <button class="burger-btn" id="burgerToggle" aria-label="Открыть меню навигации" aria-expanded="false">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Off-Canvas Drawer Navigation with Blur Backdrop (No accidental content overlap!) -->
  <div class="drawer-backdrop" id="drawerBackdrop"></div>
  <aside class="drawer-panel" id="drawerPanel" aria-label="Боковое меню">
    <div class="drawer-header">
      <div class="drawer-title">
        <span>⚡ НАВИГАЦИЯ ВОРОНКИ</span>
      </div>
      <button class="drawer-close" id="drawerClose" aria-label="Закрыть меню">✕</button>
    </div>

    <div class="drawer-nav">
      <div class="drawer-category" data-i18n="menu_cat_offer">ОФФЕР И АНАЛИТИКА</div>
      <a href="#hero" class="drawer-link" data-close>
        <span><span class="num">01</span> <span data-i18n="nav_01">Главный бриф & SoV</span></span>
        <span class="tag">Brief</span>
      </a>
      <a href="#kpis" class="drawer-link" data-close>
        <span><span class="num">02</span> <span data-i18n="nav_02">Ключевые KPI и стадии</span></span>
        <span class="tag">Metrics</span>
      </a>
      <a href="#analytics" class="drawer-link" data-close>
        <span><span class="num">03</span> <span data-i18n="nav_03">Верифицированная аналитика 90д</span></span>
        <span class="tag">Plausible</span>
      </a>
      <a href="#audience" class="drawer-link" data-close>
        <span><span class="num">04</span> <span data-i18n="nav_05">Устройства, ГЕО и Прайм-тайм</span></span>
        <span class="tag">Audience</span>
      </a>

      <div class="drawer-category" data-i18n="menu_cat_funnel">ВОРОНКА И ПРОДУКТ</div>
      <a href="#calculator" class="drawer-link" data-close>
        <span><span class="num">05</span> <span data-i18n="nav_06">Калькулятор отдачи (ROI)</span></span>
        <span class="tag">FTD Calc</span>
      </a>
      <a href="#moat" class="drawer-link" data-close>
        <span><span class="num">06</span> <span data-i18n="nav_07_moat">Архитектурные рвы & Unit Economics</span></span>
        <span class="tag">Moat</span>
      </a>
      <a href="#roadmap" class="drawer-link" data-close>
        <span><span class="num">07</span> <span data-i18n="nav_08_road">Timeline-роадмап фичей</span></span>
        <span class="tag">Arrow</span>
      </a>
      <a href="#deals" class="drawer-link" data-close>
        <span><span class="num">08</span> <span data-i18n="nav_10_deals">Форматы сотрудничества & M&A</span></span>
        <span class="tag">Deals</span>
      </a>
    </div>

    <div class="drawer-footer">
      <a href="https://lightstream.ws" target="_blank" rel="noopener" class="btn btn-secondary" style="width:100%;" id="drawerBtnOpenApp">
        <span data-i18n="drawer_open_app">Открыть lightstream.ws ↗</span>
      </a>
      <a href="https://t.me/shitmane" target="_blank" rel="noopener" class="btn btn-primary" style="width:100%;" id="drawerBtnTg">
        <span data-i18n="drawer_write_tg">Написать фаундеру: @shitmane</span>
      </a>
    </div>
  </aside>

  <main class="container">

    <!-- Hero / The Hook -->
    <section class="hero" id="hero">
      <div class="hero-top-bar">
        <div class="hero-eyebrow">
          <span class="pulse-dot"></span>
          <span data-i18n="hero_status">Статус: Production · lightstream.ws · 0 рекламного шума</span>
        </div>
        <div class="audience-switcher" id="audienceSwitcher">
          <span class="aud-label" data-i18n="aud_label">Фокус питча:</span>
          <button type="button" class="aud-btn active" id="btnAudSponsor" onclick="setAudience('sponsor')">
            <span>🎯</span>
            <span data-i18n="aud_sponsor">Спонсорам & Брендам</span>
          </button>
          <button type="button" class="aud-btn" id="btnAudInvestor" onclick="setAudience('investor')">
            <span>💼</span>
            <span data-i18n="aud_investor">Инвесторам & M&A</span>
          </button>
        </div>
      </div>

      <h1 id="heroTitle" data-i18n="hero_title">
        Стриминг нового поколения: 100% монопольное внимание киноманов без рекламного шума
      </h1>

      <p class="hero-sub" id="heroSub" data-i18n="hero_sub">
        Пока классические медиа и перегруженные сайты теряют до 50% аудитории из-за AdBlock и баннерной слепоты, LightStream отдает весь видеоинвентарь <strong>одному генеральному партнеру</strong>. Чистый плеер 1080p Ultra, 42.5 минуты непрерывного внимания на каждый сеанс и гарантированная доставка креатива.
      </p>

      <!-- Handcrafted Annotation Callout with Sketch Arrow -->
      <div class="hero-callout-row">
        <div class="sketch-arrow-wrap">
          <svg viewBox="0 0 60 30">
            <path d="M 50,5 Q 25,25 5,15" />
            <polyline points="15,8 5,15 12,24" />
          </svg>
          <span id="heroHandNote" data-i18n="hero_hand_note">42.5 мин средний просмотр (в 18 раз дольше соцсетей)</span>
        </div>
      </div>

      <!-- Action Funnel Buttons (Corey Haines 2-CTA Hierarchy + Memo Pill) -->
      <div class="hero-cta-group">
        <a href="https://t.me/shitmane" target="_blank" rel="noopener" class="btn btn-primary" style="padding:12px 24px; font-size:14px; font-weight:600;" id="heroCtaTgLink">
          <span id="heroCtaTgText" data-i18n="hero_cta_tg">Обсудить партнерство в TG ↗</span>
        </a>
        <a href="https://lightstream.ws" target="_blank" rel="noopener" class="btn btn-secondary" style="padding:12px 22px; font-size:14px;">
          <span data-i18n="hero_cta_demo">Открыть живой кинотеатр lightstream.ws ↗</span>
        </a>
        <button type="button" class="btn btn-secondary" onclick="copyExecutiveMemo()" style="padding:12px 18px; font-size:13px; font-family:var(--mono); cursor:pointer;">
          <span>📋</span> <span data-i18n="hero_cta_memo">Скопировать One-Pager</span>
        </button>
      </div>

      <!-- Blueprint Technical Metadata Strip -->
      <div class="blueprint-specs">
        <div class="spec-item">
          <span class="spec-label" data-i18n="spec_app">Платформа</span>
          <span class="spec-val">lightstream.ws</span>
        </div>
        <div class="spec-item">
          <span class="spec-label" data-i18n="spec_stack">Техстек</span>
          <span class="spec-val">SvelteKit · Bun · Hono · HLS</span>
        </div>
        <div class="spec-item">
          <span class="spec-label" data-i18n="spec_noise">Рекламный шум</span>
          <span class="spec-val" data-i18n="spec_noise_val">0 сторонних баннеров</span>
        </div>
        <div class="spec-item">
          <span class="spec-label" data-i18n="spec_deal">Формат</span>
          <span class="spec-val" data-i18n="spec_deal_val">100% Эксклюзив / M&A</span>
        </div>
      </div>
    </section>

    <section class="section" id="kpis">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="kpi_title">Ключевые показатели и динамика масштаба</h2>
          <p class="section-desc" data-i18n="kpi_desc">
            Кинотрафик оценивается через MAU (месячный охват) и досмотры. Переключайте стадию для оценки текущего факта и планового масштаба на момент подписания контракта.
          </p>
        </div>
        <div class="stage-switch" id="stageControls">
          <button class="stage-tab active" data-stage="current" onclick="setStage('current')">Факт (Месяц 2)</button>
          <button class="stage-tab" data-stage="q4_projection" onclick="setStage('q4_projection')">Run-Rate (Q4)</button>
          <button class="stage-tab" data-stage="scale" onclick="setStage('scale')">Масштаб (Q1)</button>
        </div>
      </div>

      <div class="kpi-grid">
        <div class="sketch-card kpi-card">
          <div>
            <div class="kpi-head">
              <span class="kpi-label" data-i18n="kpi_mau_label">MAU (Месячный охват)</span>
              <span class="hand-badge">Organic</span>
            </div>
            <div class="kpi-num" id="valMau">5,400+</div>
            <div class="kpi-note" id="noteMau" data-i18n="kpi_mau_note">Органическая база киноманов</div>
          </div>
          <div class="kpi-hand-badge">
            <span data-i18n="kpi_mau_hand">★ без платного трафика</span>
          </div>
        </div>

        <div class="sketch-card kpi-card">
          <div>
            <div class="kpi-head">
              <span class="kpi-label" data-i18n="kpi_session_label">Длина киносессии</span>
              <span class="hand-badge">42.5 min</span>
            </div>
            <div class="kpi-num" id="valSession">42.5 мин</div>
            <div class="kpi-note" data-i18n="kpi_session_note">В 18 раз дольше соцсетей и прелендингов</div>
          </div>
          <div class="kpi-hand-badge">
            <span data-i18n="kpi_session_hand">★ глубокое внимание</span>
          </div>
        </div>

        <div class="sketch-card kpi-card">
          <div>
            <div class="kpi-head">
              <span class="kpi-label" data-i18n="kpi_views_label">Просмотры видео / мес</span>
              <span class="hand-badge">1080p</span>
            </div>
            <div class="kpi-num" id="valViews">18,500+</div>
            <div class="kpi-note" id="noteViews" data-i18n="kpi_views_note">100% чистые досмотры в адаптивном плеере</div>
          </div>
          <div class="kpi-hand-badge">
            <span data-i18n="kpi_views_hand">★ нативный HLS-плеер</span>
          </div>
        </div>

        <div class="sketch-card kpi-card">
          <div>
            <div class="kpi-head">
              <span class="kpi-label" data-i18n="kpi_sov_label">Share of Voice</span>
              <span class="hand-badge">Exclusive</span>
            </div>
            <div class="kpi-num">100%</div>
            <div class="kpi-note" data-i18n="kpi_sov_note">Ноль сторонних брендов, ноль конкурентных слотов</div>
          </div>
          <div class="kpi-hand-badge">
            <span data-i18n="kpi_sov_hand">★ монополия для партнера</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 2: Verified 90-Day Analytics & Feature Radar -->
    <section class="section" id="analytics">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="ana_title">Верифицированная аналитика 90 дней</h2>
          <p class="section-desc" data-i18n="ana_desc">
            Реальные данные Plausible Analytics за период 7 июля – 3 октября. Экспоненциальный рост без покупного трафика.
          </p>
        </div>
      </div>

      <!-- Verified Traffic dynamics (Full-Width Blueprint SVG) -->
      <div class="sketch-card chart-card" style="margin-bottom: 24px;">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title" data-i18n="ana_chart_title">Динамика просмотров (7 июл – 3 окт)</div>
            <div class="chart-card-sub" data-i18n="ana_chart_sub">Органический взлет в сентябре с пиком >2,100 просмотров/сутки</div>
          </div>
          <span class="hand-badge" style="color:var(--accent-green); border-color:#064e3b;">+1100% Growth ★</span>
        </div>

        <div class="svg-traffic-wrap">
          <svg viewBox="0 0 500 200" preserveAspectRatio="none">
            <defs>
              <linearGradient id="sketchBar" x1="0" y1="0" x2="0" y2="1">
                <stop offset="0%" stop-color="#ffffff" stop-opacity="0.95"/>
                <stop offset="100%" stop-color="#717180" stop-opacity="0.3"/>
              </linearGradient>
            </defs>
            <!-- Dashed Blueprint Gridlines -->
            <line x1="0" y1="40" x2="500" y2="40" stroke="#252632" stroke-dasharray="4 4"/>
            <line x1="0" y1="90" x2="500" y2="90" stroke="#252632" stroke-dasharray="4 4"/>
            <line x1="0" y1="140" x2="500" y2="140" stroke="#252632" stroke-dasharray="4 4"/>
            <line x1="0" y1="180" x2="500" y2="180" stroke="#3a3b48"/>

            <!-- Sketch Bars -->
            <rect x="35" y="170" width="40" height="10" rx="3" fill="#252632" stroke="#3a3b48" stroke-width="1"/>
            <rect x="125" y="145" width="40" height="35" rx="3" fill="#323340" stroke="#454656" stroke-width="1"/>
            <rect x="215" y="115" width="40" height="65" rx="3" fill="#424354" stroke="#5a5b70" stroke-width="1"/>
            <rect x="305" y="25" width="45" height="155" rx="4" fill="url(#sketchBar)" stroke="#ffffff" stroke-width="1.5"/>
            <rect x="395" y="80" width="40" height="100" rx="3" fill="#626376" stroke="#7e7f96" stroke-width="1"/>

            <!-- Hand-drawn Peak Callout -->
            <circle cx="327" cy="25" r="4.5" fill="#fafafa"/>
            <line x1="327" y1="25" x2="327" y2="10" stroke="#fafafa" stroke-width="1.5"/>
            <text x="327" y="6" fill="#fafafa" font-size="11" font-family="'Caveat', cursive" text-anchor="middle" font-weight="700">★ Рекорд 2.1k / день</text>

            <!-- Month Labels -->
            <text x="55" y="196" fill="#717180" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Июль</text>
            <text x="145" y="196" fill="#717180" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Авг (1-15)</text>
            <text x="235" y="196" fill="#717180" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Авг (16-31)</text>
            <text x="327" y="196" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Сентябрь</text>
            <text x="415" y="196" fill="#717180" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Октябрь</text>
          </svg>
        </div>

        <div class="chart-footer-stats">
          <div>
            <div class="c-stat-k" data-i18n="stat_views">Просмотры</div>
            <div class="c-stat-v">26.6k</div>
          </div>
          <div>
            <div class="c-stat-k" data-i18n="stat_sessions">Сессии</div>
            <div class="c-stat-v">5.82k</div>
          </div>
          <div>
            <div class="c-stat-k" data-i18n="stat_uniques">Уники</div>
            <div class="c-stat-v">2.88k</div>
          </div>
          <div>
            <div class="c-stat-k" data-i18n="stat_duration">Глубина</div>
            <div class="c-stat-v">4m 18s</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Audience Devices & GEO Split -->
    <section class="section" id="audience">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="aud_title">Устройства, браузеры и географический сплит</h2>
          <p class="section-desc" data-i18n="aud_desc">
            Разделение по платежеспособности аудитории, используемым устройствам и платежным шлюзам.
          </p>
        </div>
      </div>

      <div class="devices-geo-grid">
        <!-- Browsers & Devices -->
        <div class="sketch-card chart-card">
          <div class="chart-card-header">
            <div>
              <div class="chart-card-title" data-i18n="aud_dev_title">Браузеры и окружение зрителей</div>
              <div class="chart-card-sub" data-i18n="aud_dev_sub">Десктопный и премиальный iOS трафик</div>
            </div>
            <span class="hand-badge">Tech Profile</span>
          </div>

          <div class="progress-list">
            <div class="progress-row">
              <div class="progress-labels">
                <span>💻 Google Chrome (Desktop / Win / Mac)</span>
                <span>43% (1,210)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 43%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>📱 iOS Safari (iPhone / iPad)</span>
                <span>19% (538)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 19%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>📱 iOS Webview (Telegram / In-App)</span>
                <span>14% (391)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 14%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>🌐 Chrome Webview & Другие</span>
                <span>9% (254)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 9%;"></div></div>
            </div>
          </div>
        </div>

        <!-- Geo distribution -->
        <div class="sketch-card chart-card">
          <div class="chart-card-header">
            <div>
              <div class="chart-card-title" data-i18n="aud_geo_title">Верифицированная география аудитории</div>
              <div class="chart-card-sub" data-i18n="aud_geo_sub">Сплит по странам и среднему чеку</div>
            </div>
            <span class="hand-badge">Top GEOs</span>
          </div>

          <div class="progress-list">
            <div class="progress-row">
              <div class="progress-labels">
                <span>🇺🇸 США (United States) · Tier-1</span>
                <span>24% (499)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 24%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>🇧🇾 Беларусь (Belarus) · Tier-1 CIS</span>
                <span>14% (294)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 14%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>🇺🇦 Украина (Ukraine) · Tier-1 CIS</span>
                <span>14% (291)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 14%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>🇰🇿 Казахстан (Kazakhstan) · Tier-2</span>
                <span>12% (247)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 12%;"></div></div>
            </div>

            <div class="progress-row">
              <div class="progress-labels">
                <span>🇵🇱 Польша & ЕС (Poland) · Tier-1 EU</span>
                <span>11% (222)</span>
              </div>
              <div class="progress-track"><div class="progress-fill" style="width: 11%;"></div></div>
            </div>
          </div>
        </div>
      </div>

      <!-- Audience Interactive Heatmap Matrix & Prime-Time Inspector -->
      <div class="sketch-card heat-card" id="heatmapWidget">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title" data-i18n="prime_title">Интерактивная карта внимания & Prime-Time (Heatmap Matrix)</div>
            <div class="chart-card-sub" data-i18n="prime_sub">Кликните по любому тайм-слоту (дни недели × часы) для инспекции телеметрии, длительности сессий и Share of Voice.</div>
          </div>
          <span class="hand-badge" style="color:var(--accent-green); border-color:#064e3b;" data-i18n="prime_badge">★ 19:00 – 23:30 Prime-Time (64% эфира)</span>
        </div>

        <!-- Scenario Presets & Legend Toolbar -->
        <div class="heat-toolbar">
          <div class="heat-presets">
            <button type="button" class="heat-preset-btn active" id="presetPrime" onclick="applyHeatPreset('prime')" data-i18n="heat_pre_prime">★ Вечерний Prime-Time</button>
            <button type="button" class="heat-preset-btn" id="presetLunch" onclick="applyHeatPreset('lunch')" data-i18n="heat_pre_lunch">⚡ Среда 14:00 Lunch Spike</button>
            <button type="button" class="heat-preset-btn" id="presetWeekend" onclick="applyHeatPreset('weekend')" data-i18n="heat_pre_weekend">🍿 Weekend Кинозал</button>
            <button type="button" class="heat-preset-btn" id="presetNight" onclick="applyHeatPreset('night')" data-i18n="heat_pre_night">🌙 Ночные сеансы</button>
            <button type="button" class="heat-preset-btn" id="presetAll" onclick="applyHeatPreset('all')" data-i18n="heat_pre_all">🔄 Сброс</button>
          </div>
          <div class="heat-legend">
            <span data-i18n="heat_leg_title">Активность:</span>
            <div class="heat-legend-dots">
              <span class="heat-dot heat-lvl-1" title="0-20%"></span>
              <span class="heat-dot heat-lvl-2" title="20-40%"></span>
              <span class="heat-dot heat-lvl-3" title="40-65%"></span>
              <span class="heat-dot heat-lvl-4" title="65-85%"></span>
              <span class="heat-dot heat-lvl-5" title="85-100% Пик"></span>
            </div>
            <span style="color:#fafafa; font-weight:600;" data-i18n="heat_leg_peak">Пик эфира</span>
          </div>
        </div>

        <!-- 2-Column Interactive Main Grid -->
        <div class="heat-main-grid">
          <!-- 7x12 Heatmap Matrix Table -->
          <div class="heat-table-wrap">
            <table class="heat-table" id="heatTable">
              <thead>
                <tr>
                  <th class="heat-th" style="text-align:left;" data-i18n="heat_th_day">День</th>
                  <th class="heat-th">00ч</th>
                  <th class="heat-th">02ч</th>
                  <th class="heat-th">04ч</th>
                  <th class="heat-th">06ч</th>
                  <th class="heat-th">08ч</th>
                  <th class="heat-th">10ч</th>
                  <th class="heat-th">12ч</th>
                  <th class="heat-th">14ч</th>
                  <th class="heat-th">16ч</th>
                  <th class="heat-th prime">18ч</th>
                  <th class="heat-th prime">20ч★</th>
                  <th class="heat-th prime">22ч★</th>
                </tr>
              </thead>
              <tbody id="heatTableBody">
                <!-- Dynamically generated or fallback rows -->
                <tr data-day-key="mon">
                  <td class="heat-day-lbl">Пн</td>
                  <td class="heat-cell heat-lvl-1" data-d="mon" data-h="0" data-idx="16"></td>
                  <td class="heat-cell heat-lvl-1" data-d="mon" data-h="2" data-idx="11"></td>
                  <td class="heat-cell heat-lvl-1" data-d="mon" data-h="4" data-idx="7"></td>
                  <td class="heat-cell heat-lvl-1" data-d="mon" data-h="6" data-idx="9"></td>
                  <td class="heat-cell heat-lvl-2" data-d="mon" data-h="8" data-idx="21"></td>
                  <td class="heat-cell heat-lvl-2" data-d="mon" data-h="10" data-idx="32"></td>
                  <td class="heat-cell heat-lvl-3" data-d="mon" data-h="12" data-idx="48"></td>
                  <td class="heat-cell heat-lvl-3" data-d="mon" data-h="14" data-idx="52"></td>
                  <td class="heat-cell heat-lvl-3" data-d="mon" data-h="16" data-idx="46"></td>
                  <td class="heat-cell heat-lvl-4" data-d="mon" data-h="18" data-idx="72"></td>
                  <td class="heat-cell heat-lvl-4" data-d="mon" data-h="20" data-idx="84"></td>
                  <td class="heat-cell heat-lvl-4" data-d="mon" data-h="22" data-idx="76"></td>
                </tr>
                <tr data-day-key="tue">
                  <td class="heat-day-lbl">Вт</td>
                  <td class="heat-cell heat-lvl-1" data-d="tue" data-h="0" data-idx="18"></td>
                  <td class="heat-cell heat-lvl-1" data-d="tue" data-h="2" data-idx="12"></td>
                  <td class="heat-cell heat-lvl-1" data-d="tue" data-h="4" data-idx="8"></td>
                  <td class="heat-cell heat-lvl-1" data-d="tue" data-h="6" data-idx="10"></td>
                  <td class="heat-cell heat-lvl-2" data-d="tue" data-h="8" data-idx="23"></td>
                  <td class="heat-cell heat-lvl-2" data-d="tue" data-h="10" data-idx="35"></td>
                  <td class="heat-cell heat-lvl-3" data-d="tue" data-h="12" data-idx="50"></td>
                  <td class="heat-cell heat-lvl-3" data-d="tue" data-h="14" data-idx="58"></td>
                  <td class="heat-cell heat-lvl-3" data-d="tue" data-h="16" data-idx="49"></td>
                  <td class="heat-cell heat-lvl-4" data-d="tue" data-h="18" data-idx="76"></td>
                  <td class="heat-cell heat-lvl-4" data-d="tue" data-h="20" data-idx="88"></td>
                  <td class="heat-cell heat-lvl-4" data-d="tue" data-h="22" data-idx="79"></td>
                </tr>
                <tr data-day-key="wed">
                  <td class="heat-day-lbl record">Ср ★</td>
                  <td class="heat-cell heat-lvl-2" data-d="wed" data-h="0" data-idx="24"></td>
                  <td class="heat-cell heat-lvl-1" data-d="wed" data-h="2" data-idx="15"></td>
                  <td class="heat-cell heat-lvl-1" data-d="wed" data-h="4" data-idx="9"></td>
                  <td class="heat-cell heat-lvl-1" data-d="wed" data-h="6" data-idx="14"></td>
                  <td class="heat-cell heat-lvl-2" data-d="wed" data-h="8" data-idx="28"></td>
                  <td class="heat-cell heat-lvl-2" data-d="wed" data-h="10" data-idx="41"></td>
                  <td class="heat-cell heat-lvl-3" data-d="wed" data-h="12" data-idx="62"></td>
                  <td class="heat-cell heat-lvl-5" data-d="wed" data-h="14" data-idx="94" title="14:00 Lunch Spike (+45%)"></td>
                  <td class="heat-cell heat-lvl-3" data-d="wed" data-h="16" data-idx="59"></td>
                  <td class="heat-cell heat-lvl-4" data-d="wed" data-h="18" data-idx="82"></td>
                  <td class="heat-cell heat-lvl-5 is-selected" data-d="wed" data-h="20" data-idx="100" title="20:00 Абсолютный пик недели"></td>
                  <td class="heat-cell heat-lvl-5" data-d="wed" data-h="22" data-idx="92"></td>
                </tr>
                <tr data-day-key="thu">
                  <td class="heat-day-lbl">Чт</td>
                  <td class="heat-cell heat-lvl-1" data-d="thu" data-h="0" data-idx="19"></td>
                  <td class="heat-cell heat-lvl-1" data-d="thu" data-h="2" data-idx="13"></td>
                  <td class="heat-cell heat-lvl-1" data-d="thu" data-h="4" data-idx="8"></td>
                  <td class="heat-cell heat-lvl-1" data-d="thu" data-h="6" data-idx="11"></td>
                  <td class="heat-cell heat-lvl-2" data-d="thu" data-h="8" data-idx="24"></td>
                  <td class="heat-cell heat-lvl-2" data-d="thu" data-h="10" data-idx="36"></td>
                  <td class="heat-cell heat-lvl-3" data-d="thu" data-h="12" data-idx="52"></td>
                  <td class="heat-cell heat-lvl-3" data-d="thu" data-h="14" data-idx="56"></td>
                  <td class="heat-cell heat-lvl-3" data-d="thu" data-h="16" data-idx="51"></td>
                  <td class="heat-cell heat-lvl-4" data-d="thu" data-h="18" data-idx="78"></td>
                  <td class="heat-cell heat-lvl-4" data-d="thu" data-h="20" data-idx="89"></td>
                  <td class="heat-cell heat-lvl-4" data-d="thu" data-h="22" data-idx="81"></td>
                </tr>
                <tr data-day-key="fri">
                  <td class="heat-day-lbl">Пт ★</td>
                  <td class="heat-cell heat-lvl-2" data-d="fri" data-h="0" data-idx="28"></td>
                  <td class="heat-cell heat-lvl-1" data-d="fri" data-h="2" data-idx="18"></td>
                  <td class="heat-cell heat-lvl-1" data-d="fri" data-h="4" data-idx="10"></td>
                  <td class="heat-cell heat-lvl-1" data-d="fri" data-h="6" data-idx="12"></td>
                  <td class="heat-cell heat-lvl-2" data-d="fri" data-h="8" data-idx="25"></td>
                  <td class="heat-cell heat-lvl-2" data-d="fri" data-h="10" data-idx="38"></td>
                  <td class="heat-cell heat-lvl-3" data-d="fri" data-h="12" data-idx="54"></td>
                  <td class="heat-cell heat-lvl-3" data-d="fri" data-h="14" data-idx="60"></td>
                  <td class="heat-cell heat-lvl-3" data-d="fri" data-h="16" data-idx="58"></td>
                  <td class="heat-cell heat-lvl-4" data-d="fri" data-h="18" data-idx="85"></td>
                  <td class="heat-cell heat-lvl-5" data-d="fri" data-h="20" data-idx="97" title="Ночной кинозал"></td>
                  <td class="heat-cell heat-lvl-5" data-d="fri" data-h="22" data-idx="95"></td>
                </tr>
                <tr data-day-key="sat">
                  <td class="heat-day-lbl">Сб</td>
                  <td class="heat-cell heat-lvl-2" data-d="sat" data-h="0" data-idx="34"></td>
                  <td class="heat-cell heat-lvl-2" data-d="sat" data-h="2" data-idx="22"></td>
                  <td class="heat-cell heat-lvl-1" data-d="sat" data-h="4" data-idx="12"></td>
                  <td class="heat-cell heat-lvl-1" data-d="sat" data-h="6" data-idx="11"></td>
                  <td class="heat-cell heat-lvl-2" data-d="sat" data-h="8" data-idx="22"></td>
                  <td class="heat-cell heat-lvl-2" data-d="sat" data-h="10" data-idx="42"></td>
                  <td class="heat-cell heat-lvl-3" data-d="sat" data-h="12" data-idx="64"></td>
                  <td class="heat-cell heat-lvl-3" data-d="sat" data-h="14" data-idx="68"></td>
                  <td class="heat-cell heat-lvl-4" data-d="sat" data-h="16" data-idx="74"></td>
                  <td class="heat-cell heat-lvl-4" data-d="sat" data-h="18" data-idx="88"></td>
                  <td class="heat-cell heat-lvl-5" data-d="sat" data-h="20" data-idx="98" title="Семейный уикенд"></td>
                  <td class="heat-cell heat-lvl-5" data-d="sat" data-h="22" data-idx="94"></td>
                </tr>
                <tr data-day-key="sun">
                  <td class="heat-day-lbl">Вс</td>
                  <td class="heat-cell heat-lvl-2" data-d="sun" data-h="0" data-idx="30"></td>
                  <td class="heat-cell heat-lvl-1" data-d="sun" data-h="2" data-idx="17"></td>
                  <td class="heat-cell heat-lvl-1" data-d="sun" data-h="4" data-idx="10"></td>
                  <td class="heat-cell heat-lvl-1" data-d="sun" data-h="6" data-idx="9"></td>
                  <td class="heat-cell heat-lvl-2" data-d="sun" data-h="8" data-idx="20"></td>
                  <td class="heat-cell heat-lvl-2" data-d="sun" data-h="10" data-idx="39"></td>
                  <td class="heat-cell heat-lvl-3" data-d="sun" data-h="12" data-idx="61"></td>
                  <td class="heat-cell heat-lvl-3" data-d="sun" data-h="14" data-idx="66"></td>
                  <td class="heat-cell heat-lvl-4" data-d="sun" data-h="16" data-idx="72"></td>
                  <td class="heat-cell heat-lvl-4" data-d="sun" data-h="18" data-idx="86"></td>
                  <td class="heat-cell heat-lvl-5" data-d="sun" data-h="20" data-idx="96"></td>
                  <td class="heat-cell heat-lvl-4" data-d="sun" data-h="22" data-idx="82"></td>
                </tr>
              </tbody>
            </table>
          </div>

          <!-- Live Interactive Telemetry Inspector Card -->
          <div class="heat-inspector" id="heatInspector">
            <div>
              <div class="insp-header">
                <div>
                  <div class="insp-slot-title" id="inspSlotTitle">Среда · 20:00 – 22:00</div>
                  <div class="insp-slot-status" id="inspSlotStatus">★ Абсолютный пик недели (Киносеанс)</div>
                </div>
                <span class="pm-pill" style="color:#fafafa; border:1px solid #3f4055; background:rgba(255,255,255,0.06);" id="inspTagSlot">100% SoV</span>
              </div>

              <!-- Engagement Index Gauge -->
              <div class="insp-gauge-wrap">
                <div class="insp-gauge-head">
                  <span data-i18n="insp_gauge_lbl">Индекс вовлеченности & эфира</span>
                  <strong style="color:#fafafa;" id="inspIdxVal">100 / 100</strong>
                </div>
                <div class="insp-gauge-track">
                  <div class="insp-gauge-fill" id="inspGaugeFill" style="width: 100%;"></div>
                </div>
              </div>

              <!-- 4 Telemetry Metrics Grid -->
              <div class="insp-metrics-grid">
                <div class="insp-m-item">
                  <div class="insp-m-k" data-i18n="insp_m_session">Длительность сессии</div>
                  <div class="insp-m-v" id="inspSessionVal">48.5 мин</div>
                </div>
                <div class="insp-m-item">
                  <div class="insp-m-k" data-i18n="insp_m_devices">Большие экраны</div>
                  <div class="insp-m-v" id="inspDeviceVal">64% Smart TV & PC</div>
                </div>
                <div class="insp-m-item">
                  <div class="insp-m-k" data-i18n="insp_m_sov">Share of Voice</div>
                  <div class="insp-m-v" id="inspSovVal" style="color:var(--accent-green);">100% Exclusive</div>
                </div>
                <div class="insp-m-item">
                  <div class="insp-m-k" data-i18n="insp_m_retention">AdBlock Bypass</div>
                  <div class="insp-m-v" id="inspAdblockVal">100% Доставка</div>
                </div>
              </div>
            </div>

            <!-- Investor / Sponsor Context Memo -->
            <div class="insp-tip" id="inspDesc">
              «Золотое окно полного внимания. Пользователи смотрят полнометражные премьеры на больших экранах без перемотки. Премиальный слот для монопольного брендинга и нативных pre-roll вставок без потерь от блокировщиков.»
            </div>
          </div>
        </div>

        <!-- 3 Key Takeaways -->
        <div class="heat-takeaways">
          <div class="heat-takeaway-card">
            <span class="heat-takeaway-tag" data-i18n="prime_c1_tag">Прайм-слот 19:00 – 23:30</span>
            <div class="heat-takeaway-val" data-i18n="prime_c1_val">64% суточного эфира</div>
            <div class="heat-takeaway-desc" data-i18n="prime_c1_desc">Максимальная вовлеченность. Просмотр полнометражных фильмов со средней длительностью сессии 42+ мин.</div>
          </div>
          <div class="heat-takeaway-card">
            <span class="heat-takeaway-tag" data-i18n="prime_c2_tag">Среда 14:00 Lunch Spike</span>
            <div class="heat-takeaway-val" data-i18n="prime_c2_val">+45% дневной всплеск</div>
            <div class="heat-takeaway-desc" data-i18n="prime_c2_desc">Аномальный всплеск дневного внимания в середине рабочей недели (обеденный тайм-аут и фоновые просмотры сериалов).</div>
          </div>
          <div class="heat-takeaway-card">
            <span class="heat-takeaway-tag" data-i18n="prime_c3_tag">Desktop & Smart TV</span>
            <div class="heat-takeaway-val" data-i18n="prime_c3_val">58% большие экраны</div>
            <div class="heat-takeaway-desc" data-i18n="prime_c3_desc">В вечернее время аудитория переключается на полноэкранный режим, обеспечивая абсолютный 100% Share of Voice.</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 4: Interactive Sponsor ROI Calculator -->
    <section class="section" id="calculator">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="calc_title">Интерактивный калькулятор отдачи (ROI)</h2>
          <p class="section-desc" data-i18n="calc_desc">
            Оцените отдачу от 100% Share of Voice в плеере LightStream при масштабировании аудитории до целевых значений.
          </p>
        </div>
      </div>

      <div class="sketch-card calc-box">
        <div class="calc-grid">
          <div class="calc-slider-wrap">
            <label>
              <span data-i18n="calc_lbl_mau">Месячный охват аудитории (MAU)</span>
              <span><strong id="calcMauDisplay">45,000</strong> зрителей</span>
            </label>
            <input type="range" min="5000" max="150000" step="5000" value="45000" class="calc-slider" id="sliderMau">
          </div>

          <div class="calc-slider-wrap">
            <label>
              <span data-i18n="calc_lbl_ctr">Конверсия в переход из плеера (CTR)</span>
              <span><strong id="calcCtrDisplay">3.5%</strong> (нативный оверлей)</span>
            </label>
            <input type="range" min="1.0" max="7.0" step="0.5" value="3.5" class="calc-slider" id="sliderCtr">
          </div>
        </div>

        <div class="calc-results-row">
          <div class="res-item">
            <div class="res-lbl" data-i18n="res_lbl_imp">Видео-показы / мес</div>
            <div class="res-val" id="resImpressions">160,000</div>
            <div class="res-sub">100% Share of Voice</div>
          </div>
          <div class="res-item">
            <div class="res-lbl" data-i18n="res_lbl_clk">Прямые клики на оффер</div>
            <div class="res-val" id="resClicks">5,600</div>
            <div class="res-sub" data-i18n="res_sub_adblock">Без потерь на AdBlock</div>
          </div>
          <div class="res-item">
            <div class="res-lbl" data-i18n="res_lbl_ftd">Прогноз FTD (Депозитов)</div>
            <div class="res-val" id="resFtd">336 – 560</div>
            <div class="res-sub">CR 6–10% рег2деп</div>
          </div>
          <div class="res-item">
            <div class="res-lbl" data-i18n="res_lbl_val">Ценность трафика (CPA экв.)</div>
            <div class="res-val" id="resVal">$16,800+</div>
            <div class="res-sub">При ставке $40 FTD</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section: Defensive Moats & Unit Economics -->
    <section class="section" id="moat">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="moat_title">Архитектурные рвы & Unit Economics</h2>
          <p class="section-desc" data-i18n="moat_desc">
            Почему LightStream защищен от вытеснения: нулевые затраты на хранение видео, органический CAC $0 и высокий барьер удержания.
          </p>
        </div>
        <span class="hand-badge" data-i18n="moat_hand_badge">★ 88% Gross Margin Moat</span>
      </div>

      <div class="moat-grid">
        <!-- Card 1: Zero Storage Capex -->
        <div class="moat-card">
          <div class="moat-head">
            <span class="moat-title" data-i18n="moat_c1_t">Zero-Storage Capex: Edge CDN Routing</span>
            <span class="moat-badge">Capex $0</span>
          </div>
          <p class="moat-desc" data-i18n="moat_c1_d">
            Классические OTT тратят миллионы на AWS S3 и транскодинг петабайт видео. LightStream балансирует между распределенными CDN-нодами и внешними стримами. Нулевой счет за хостинг видео при каталоге 100,000+ тайтлов.
          </p>
          <div class="moat-box-comp">
            <div class="moat-row">
              <span class="moat-lbl" data-i18n="moat_lbl_ott">Классический OTT (AWS S3)</span>
              <span class="moat-val-bad" data-i18n="moat_val_ott_cost">$120,000+ / мес</span>
            </div>
            <div class="moat-row">
              <span class="moat-lbl">LightStream Edge Balancer</span>
              <span class="moat-val-good" data-i18n="moat_val_ls_cost">≈ $0 (Egress-neutral)</span>
            </div>
          </div>
        </div>

        <!-- Card 2: Organic Flywheel & CAC = $0 -->
        <div class="moat-card">
          <div class="moat-head">
            <span class="moat-title" data-i18n="moat_c2_t">Органический маховик & CAC = $0</span>
            <span class="moat-badge">CAC = $0</span>
          </div>
          <p class="moat-desc" data-i18n="moat_c2_d">
            Нулевые затраты на платную рекламу. Привлечение через киноманские комьюнити, партизанский маркетинг в соцсетях, вирусные нарезки сцен и сарафанное радио за счет чистого плеера без скам-баннеров.
          </p>
          <div class="moat-box-comp">
            <div class="moat-row">
              <span class="moat-lbl" data-i18n="moat_lbl_market_cac">Средний CAC в индустрии</span>
              <span class="moat-val-bad">$28 – $45 / юзер</span>
            </div>
            <div class="moat-row">
              <span class="moat-lbl">LightStream Blended CAC</span>
              <span class="moat-val-good">$0.00 (Органика)</span>
            </div>
          </div>
        </div>

        <!-- Card 3: EdTech Switching Barrier -->
        <div class="moat-card">
          <div class="moat-head">
            <span class="moat-title" data-i18n="moat_c3_t">Барьер удержания: EdTech Lock-In</span>
            <span class="moat-badge">Retention Moat</span>
          </div>
          <p class="moat-desc" data-i18n="moat_c3_d">
            Smart Subtitles с переводом по клику и личный словарь превращают развлечение в образовательный инструмент. Пользователь накапливает базу изученных слов и историю TMDB — уйти на другой сервис значит потерять прогресс.
          </p>
          <div class="moat-box-comp">
            <div class="moat-row">
              <span class="moat-lbl" data-i18n="moat_lbl_stickiness">LTV мультипликатор</span>
              <span class="moat-val-good">+3.4x vs Обычный просмотр</span>
            </div>
            <div class="moat-row">
              <span class="moat-lbl" data-i18n="moat_lbl_churn">Отток (Churn Rate)</span>
              <span class="moat-val-good">-42% среди пользователей субтитров</span>
            </div>
          </div>
        </div>

        <!-- Card 4: 100% AdBlock Immunity -->
        <div class="moat-card">
          <div class="moat-head">
            <span class="moat-title" data-i18n="moat_c4_t">100% Иммунитет к AdBlock & SoV</span>
            <span class="moat-badge">100% SoV</span>
          </div>
          <p class="moat-desc" data-i18n="moat_c4_d">
            Интеграция спонсорства нативно на уровне платформы и плеера, без сторонних рекламных скриптов и фреймов, которые блокируются uBlock Origin и браузером Brave. Гарантированный 100% контакт с аудиторией.
          </p>
          <div class="moat-box-comp">
            <div class="moat-row">
              <span class="moat-lbl" data-i18n="moat_lbl_adblock_loss">Потери трафика на сайтах (AdBlock)</span>
              <span class="moat-val-bad">-48% баннеров скрыто</span>
            </div>
            <div class="moat-row">
              <span class="moat-lbl">LightStream Доставляемость</span>
              <span class="moat-val-good">100% Доставка креатива</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: Feature Roadmap (Vertical Arrow Stem according to reference) -->
    <section class="section" id="roadmap">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="road_title">Timeline-роадмап фичей</h2>
          <p class="section-desc" data-i18n="road_desc">
            Вектор развития продукта: от уже запущенного видеодвижка до социальных и ИИ-инноваций следующего поколения. Без абстрактных дат — строго по фичам и статусам внедрения.
          </p>
        </div>
        <span class="hand-badge" data-i18n="road_hand_badge">★ 01–08 Архитектура & Фичи</span>
      </div>

      <div class="timeline-wrap">
        <div class="timeline-stem"></div>

        <!-- 01: Largest Library & Multi-CDN Player (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-done">01</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge done" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Largest Library & Engine</span>
            </div>
            <div class="t-title" data-i18n="rm_01_t">Самая большая библиотека & Мульти-CDN плеер</div>
            <div class="t-desc" data-i18n="rm_01_d">
              Агрегация всех CDN-балансеров в едином адаптивном HLS/DASH плеере: автопереключение источников при сбоях, 1080p, мгновенный старт. Все топовые русские озвучки (Red Head Sound, LostFilm, HDRezka, Кубик в Кубе) + оригинальный звук.
            </div>
          </div>
        </div>

        <!-- 02: 2-Way TMDB Sync & Omnibox (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-done">02</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge done" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">2-Way TMDB Sync</span>
            </div>
            <div class="t-title" data-i18n="rm_02_t">Двусторонняя синхронизация с TMDB & Живой поиск</div>
            <div class="t-desc" data-i18n="rm_02_d">
              Мгновенный Omnibox-поиск любого фильма, сериала или аниме прямо на сайте. Полные карточки: актеры, фильмографии, бюджеты, рейтинги, кадры, трейлеры и факты. Двусторонняя синхронизация списков и каталогов в реальном времени.
            </div>
          </div>
        </div>

        <!-- 03: Smart Bilingual Subs & Language Learning (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-done">03</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge done" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Smart Subtitles & EdTech</span>
            </div>
            <div class="t-title" data-i18n="rm_03_t">Smart Subtitles & Изучение языка по кино</div>
            <div class="t-desc" data-i18n="rm_03_d">
              Двойные параллельные субтитры RU + EN. Мгновенный перевод любого незнакомого слова по клику или тапу прямо во время просмотра. Интерактивный личный словарь и сохранение вордлистов для прокачки английского по фильмам.
            </div>
          </div>
        </div>

        <!-- 04: Custom Subtitles (.srt/.vtt) & Skip Intro (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-done">04</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge done" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Custom Subs & IntroDB</span>
            </div>
            <div class="t-title" data-i18n="rm_04_t">Свои субтитры (.srt/.vtt) & Skip Intro (TheIntroDB)</div>
            <div class="t-desc" data-i18n="rm_04_d">
              Возможность загрузить собственные файлы субтитров к любому тайтлу прямо в плеер. Автоматический пропуск опенингов и заставок сериалов в один клик через базу TheIntroDB без ручной перемотки.
            </div>
          </div>
        </div>

        <!-- 05: Cloud Library & Second-Accurate Sync (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-done">05</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge done" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Cloud Library & Sync</span>
            </div>
            <div class="t-title" data-i18n="rm_05_t">Облачная библиотека & Точный синк до секунды</div>
            <div class="t-desc" data-i18n="rm_05_d">
              Умные закладки, папки («Буду смотреть», «Избранное»), история просмотров и функция «Продолжить просмотр» с точностью до секунды. Бесшовная кросс-девайс синхронизация между ПК, смартфоном и планшетом. Персональные AI-рекомендации.
            </div>
          </div>
        </div>

        <!-- 06: Live AI Subs & Voice EQ (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-wip">06</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge wip" data-i18n="st_wip">В работе ⚡</span>
              <span class="t-stage">AI Audio & Subtitle Engine</span>
            </div>
            <div class="t-title" data-i18n="rm_06_t">AI-перевод субтитров на лету & Voice EQ</div>
            <div class="t-desc" data-i18n="rm_06_d">
              Мгновенная генерация и перевод субтитров нейросетями для свежайших мировых премьер, у которых еще нет официального дубляжа. Ночной режим нормализации звука: четкие диалоги поверх оглушающих спецэффектов.
            </div>
          </div>
        </div>

        <!-- 07: Watch Party & Timestamp Share (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-wip">07</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge wip" data-i18n="st_wip">В работе ⚡</span>
              <span class="t-stage">Social Streaming & Sharing</span>
            </div>
            <div class="t-title" data-i18n="rm_07_t">Social Watch Party & Таймкод-шаринг моментов</div>
            <div class="t-desc" data-i18n="rm_07_d">
              Синхронный совместный просмотр фильмов и сериалов с друзьями по одной ссылке: единая перемотка, реакции и текстово-голосовой чат. Мгновенный шаринг любимых сцен с точным таймкодом и цитатами.
            </div>
          </div>
        </div>

        <!-- 08: Semantic AI Search & Multi-Profiles (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-plan">08</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge plan" data-i18n="st_plan">Запланировано</span>
              <span class="t-stage">Semantic Discovery & Multi-Profile</span>
            </div>
            <div class="t-title" data-i18n="rm_08_t">Семантический AI-поиск по вайбу & Мультипрофили</div>
            <div class="t-desc" data-i18n="rm_08_d">
              Умный подбор кино на естественном языке по настроению и скрытому смыслу («напряженный детектив в дождливом городе с неожиданным финалом»). Семейные изолированные профили с раздельной историей и рекомендациями.
            </div>
          </div>
        </div>
      </div>

      <!-- Final Goal Milestone Card -->
      <div class="timeline-grand">
        <div class="sketch-card grand-card">
          <span class="t-badge done" style="background:#fafafa; color:#09090c; font-weight:700;" data-i18n="rm_star_badge">★ Ключевая цель экосистемы</span>
          <div class="t-title" style="font-size:16px; margin:8px 0 6px;" data-i18n="rm_star_t">Создать лучший стриминговый сервис и смести конкурентов</div>
          <div class="t-desc" data-i18n="rm_star_d">
            Объединить самую большую библиотеку кино в мире, адаптивный Multi-CDN плеер с мгновенным стартом, уникальные EdTech-фичи (Smart Subtitles, синхронизация с TMDB, TheIntroDB), нулевой рекламный шум и вирусную витрину сцен. Превзойти и устаревшие пиратские помойки с вирусами, и медленные легальные онлайн-кинотеатры с урезанными каталогами и платными подписками, сделав LightStream безальтернативным выбором для киноманов.
          </div>
        </div>
      </div>
    </section>

    <!-- Executive Summary Memo Export Bar -->
    <div class="memo-bar" id="memoBar">
      <div class="memo-info">
        <div class="memo-title">
          <span>📄</span>
          <span data-i18n="memo_bar_title">Executive Summary Memo (One-Pager)</span>
        </div>
        <div class="memo-sub" data-i18n="memo_bar_sub">
          Сформировать и скопировать готовый бриф в формате Markdown для отправки в Telegram или вставки в инвестиционные заметки.
        </div>
      </div>
      <button type="button" class="memo-btn" onclick="copyExecutiveMemo()">
        <span>📋</span>
        <span data-i18n="memo_btn_txt">Скопировать One-Pager Memo</span>
      </button>
    </div>

    <!-- Section 9: Deal Options -->
    <section class="section" id="deals">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="deal_title">Форматы сотрудничества</h2>
          <p class="section-desc" data-i18n="deal_desc">
            Прозрачные модели партнерства — от фиксированного рекламного ретейнера до полной продажи актива с передачей кода и инфраструктуры.
          </p>
        </div>
      </div>

      <div class="deals-grid" id="dealsContainer">
        <!-- Rendered by JS based on language -->
      </div>
    </section>

    <!-- Bottom Direct Funnel Conversion Banner -->
    <div class="sketch-card cta-banner">
      <div class="cta-left">
        <div class="cta-title" data-i18n="cta_title">Обсудить партнерство или запросить доступ к метрикам</div>
        <div class="cta-desc" data-i18n="cta_desc">
          Мы открыты к созвону в Google Meet или диалогу в Telegram для обсуждения фиксированной ставки спонсорства, параметров CPA-бейслайна или M&A аудита платформы.
        </div>
      </div>
      <div class="cta-btns">
        <a href="https://t.me/shitmane" target="_blank" rel="noopener" class="btn btn-primary" style="padding:12px 24px; font-size:14px;">
          <span data-i18n="cta_btn_tg">Написать фаундеру: @shitmane ↗</span>
        </a>
        <a href="https://lightstream.ws" target="_blank" rel="noopener" class="btn btn-secondary" style="padding:10px 20px;">
          <span data-i18n="cta_btn_app">Открыть кинотеатр: lightstream.ws ↗</span>
        </a>
        <a href="mailto:good22067@gmail.com" class="btn btn-secondary" style="padding:8px 16px; font-family:var(--mono); font-size:12px;">
          good22067@gmail.com
        </a>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      <div>LightStream Media Group · lightstream.ws</div>
      <div id="updatedAtLabel">2026-10-05</div>
    </footer>

  </main>

  <script>
    // Bilingual Dictionaries
    const i18nData = {
      ru: {
        head_open_app: "Кинотеатр ↗",
        head_contact_tg: "Связаться в TG",
        drawer_open_app: "Открыть lightstream.ws ↗",
        drawer_write_tg: "Написать фаундеру: @shitmane",
        menu_cat_offer: "ОФФЕР И АНАЛИТИКА",
        menu_cat_funnel: "ВОРОНКА И ПРОДУКТ",
        nav_01: "Главный бриф & SoV",
        nav_02: "Ключевые KPI и стадии",
        nav_03: "Верифицированная аналитика 90д",
        nav_04: "Радар & Матрица vs Netflix",
        nav_05: "Устройства, ГЕО и Прайм-тайм",
        nav_06: "Калькулятор отдачи (ROI)",
        nav_07: "Timeline-роадмап фичей",
        nav_08: "Форматы сотрудничества & M&A",
        aud_label: "Фокус питча:",
        aud_sponsor: "Спонсорам & Брендам",
        aud_investor: "Инвесторам & M&A",
        hero_status: "Статус: Production · lightstream.ws · 0 рекламного шума",
        hero_title_sponsor: "Стриминг нового поколения: 100% монопольное внимание киноманов без рекламного шума",
        hero_sub_sponsor: "Пока классические медиа и перегруженные сайты теряют до 50% аудитории из-за AdBlock и баннерной слепоты, LightStream отдает весь видеоинвентарь <strong>одному генеральному партнеру</strong>. Чистый плеер 1080p Ultra, 42.5 минуты непрерывного внимания на каждый сеанс и гарантированная доставка креатива.",
        hero_hand_note_sponsor: "42.5 мин средний просмотр (в 18 раз дольше соцсетей)",
        hero_cta_tg_sponsor: "Обсудить партнерство в TG ↗",
        hero_title_investor: "Технологический стриминг: CAC = $0, Gross Margin 88% и фундаментальные рвы",
        hero_sub_investor: "LightStream разрушает экономику неповоротливых OTT-сервисов. Собственный мульти-CDN балансировщик сводит затраты на хранение видео к нулю, вирусные петли дают органический рост при CAC $0, а умные EdTech-субтитры увеличивают LTV зрителя в 3.4 раза.",
        hero_hand_note_investor: "★ Околонулевой burn-rate инфраструктуры + вирусная машина",
        hero_cta_tg_investor: "Запросить Data Room в TG ↗",
        hero_title: "Стриминг нового поколения: 100% монопольное внимание киноманов без рекламного шума",
        hero_sub: "Пока классические медиа и перегруженные сайты теряют до 50% аудитории из-за AdBlock и баннерной слепоты, LightStream отдает весь видеоинвентарь <strong>одному генеральному партнеру</strong>. Чистый плеер 1080p Ultra, 42.5 минуты непрерывного внимания на каждый сеанс и гарантированная доставка креатива.",
        hero_hand_note: "42.5 мин средний просмотр (в 18 раз дольше соцсетей)",
        hero_cta_tg: "Обсудить партнерство в TG ↗",
        hero_cta_demo: "Открыть живой кинотеатр lightstream.ws ↗",
        hero_cta_memo: "Скопировать One-Pager",
        hero_cta_scroll: "Метрики 90д ↓",
        spec_app: "Платформа",
        spec_stack: "Техстек",
        spec_noise: "Рекламный шум",
        spec_noise_val: "0 сторонних баннеров",
        spec_deal: "Формат",
        spec_deal_val: "100% Эксклюзив / M&A",
        pm_hand_note: "Интерактивный плеер: нажмите на слово в субтитрах или скипните интро ↷",
        pm_tag_adblock: "0% AdBlock Detection",
        pm_btn_tmdb: "TMDB Инфо",
        pm_movie_name: "Оппенгеймер (2023) · Oppenheimer",
        pm_skip_intro: "Пропустить заставку (01:42)",
        pm_pop_trans: "прорыв, решающее открытие (сущ.)",
        pm_pop_save: "+ В личный EdTech-словарь",
        pm_pop_saved: "✓ Сохранено в EdTech-словарь",
        pm_sub_before: "We are building a ",
        pm_sub_after: " streaming ecosystem for cinephiles.",
        pm_word_hint: "нажми / tap",
        pm_tmdb_title: "Карточка TMDB (2-Way Sync)",
        pm_tmdb_dir_lbl: "Режиссер:",
        pm_tmdb_cast_lbl: "В ролях:",
        pm_tmdb_budget_lbl: "Бюджет:",
        pm_tmdb_sync_desc: "Синхронизация списков и закладок с официальным аккаунтом TMDB в обе стороны.",
        pm_tmdb_sync_btn: "+ В список «Буду смотреть» (TMDB)",
        pm_tmdb_synced: "✓ Синхронизировано с TMDB",
        kpi_title: "Ключевые показатели и динамика масштаба",
        kpi_desc: "Кинотрафик оценивается через MAU (месячный охват) и досмотры. Переключайте стадию для оценки текущего факта и планового масштаба на момент подписания контракта.",
        kpi_mau_label: "MAU (Месячный охват)",
        kpi_mau_note: "Органическая база киноманов",
        kpi_mau_hand: "★ без платного трафика",
        kpi_session_label: "Длина киносессии",
        kpi_session_note: "В 18 раз дольше соцсетей и прелендингов",
        kpi_session_hand: "★ глубокое внимание",
        kpi_views_label: "Просмотры видео / мес",
        kpi_views_note: "100% чистые досмотры в адаптивном плеере",
        kpi_views_hand: "★ нативный HLS-плеер",
        kpi_sov_label: "Share of Voice",
        kpi_sov_note: "Ноль сторонних брендов, ноль конкурентных слотов",
        kpi_sov_hand: "★ монополия для партнера",
        ana_title: "Верифицированная аналитика 90 дней",
        ana_desc: "Реальные данные Plausible Analytics за период 7 июля – 3 октября. Экспоненциальный рост без покупного трафика.",
        ana_chart_title: "Динамика просмотров (7 июл – 3 окт)",
        ana_chart_sub: "Органический взлет в сентябре с пиком >2,100 просмотров/сутки",
        stat_views: "Просмотры",
        stat_sessions: "Сессии",
        stat_uniques: "Уники",
        stat_duration: "Глубина",
        radar_title: "Радар функционала: LightStream vs Netflix",
        radar_sub: "Сравнение по 6 ключевым осям стриминга и технологий",
        aud_title: "Устройства, браузеры и географический сплит",
        aud_desc: "Разделение по платежеспособности аудитории, используемым устройствам и платежным шлюзам.",
        aud_dev_title: "Браузеры и окружение зрителей",
        aud_dev_sub: "Десктопный и премиальный iOS трафик",
        aud_geo_title: "Верифицированная география аудитории",
        aud_geo_sub: "Сплит по странам и среднему чеку",
        prime_title: "Интерактивная карта внимания & Prime-Time (Heatmap Matrix)",
        prime_sub: "Кликните по любому тайм-слоту (дни недели × часы) для инспекции телеметрии, длительности сессий и Share of Voice.",
        prime_badge: "★ 19:00 – 23:30 Prime-Time (64% эфира)",
        heat_pre_prime: "★ Вечерний Prime-Time",
        heat_pre_lunch: "⚡ Среда 14:00 Lunch Spike",
        heat_pre_weekend: "🍿 Weekend Кинозал",
        heat_pre_night: "🌙 Ночные сеансы",
        heat_pre_all: "🔄 Сброс",
        heat_leg_title: "Активность:",
        heat_leg_peak: "Пик эфира",
        heat_th_day: "День",
        insp_gauge_lbl: "Индекс вовлеченности & эфира",
        insp_m_session: "Длительность сессии",
        insp_m_devices: "Большие экраны",
        insp_m_sov: "Share of Voice",
        insp_m_retention: "AdBlock Bypass",
        prime_c1_tag: "Прайм-слот 19:00 – 23:30",
        prime_c1_val: "64% суточного эфира",
        prime_c1_desc: "Максимальная вовлеченность. Просмотр полнометражных фильмов со средней длительностью сессии 42+ мин.",
        prime_c2_tag: "Среда 14:00 Lunch Spike",
        prime_c2_val: "+45% дневной всплеск",
        prime_c2_desc: "Аномальный всплеск дневного внимания в середине рабочей недели (обеденный тайм-аут и фоновые просмотры сериалов).",
        prime_c3_tag: "Desktop & Smart TV",
        prime_c3_val: "58% большие экраны",
        prime_c3_desc: "В вечернее время аудитория переключается на полноэкранный режим, обеспечивая абсолютный 100% Share of Voice.",
        calc_title: "Интерактивный калькулятор отдачи (ROI)",
        calc_desc: "Оцените отдачу от 100% Share of Voice в плеере LightStream при масштабировании аудитории до целевых значений.",
        calc_lbl_mau: "Месячный охват аудитории (MAU)",
        calc_lbl_ctr: "Конверсия в переход из плеера (CTR)",
        res_lbl_imp: "Видео-показы / мес",
        res_lbl_clk: "Прямые клики на оффер",
        res_sub_adblock: "Без потерь на AdBlock",
        res_lbl_ftd: "Прогноз FTD (Депозитов)",
        res_lbl_val: "Ценность трафика (CPA экв.)",
        mat_title: "Сравнение стека: Data instead of marketing",
        mat_desc: "Технологические возможности LightStream против устаревших пиратских плееров и Netflix.",
        th_feature: "Критерий / Фича",
        th_pirates: "Пиратские сайты",
        road_title: "Timeline-роадмап фичей",
        road_desc: "Вектор развития продукта: от уже запущенного видеодвижка до социальных и ИИ-инноваций следующего поколения. Без абстрактных дат — строго по фичам и статусам внедрения.",
        road_hand_badge: "★ 01–08 Архитектура & Фичи",
        st_done: "В проде ✓",
        st_wip: "В работе ⚡",
        st_plan: "Запланировано",
        rm_01_t: "Самая большая библиотека & Мульти-CDN плеер",
        rm_01_d: "Агрегация всех CDN-балансеров в едином адаптивном HLS/DASH плеере: автопереключение источников при сбоях, 1080p, мгновенный старт. Все топовые русские озвучки (Red Head Sound, LostFilm, HDRezka, Кубик в Кубе) + оригинальный звук.",
        rm_02_t: "Двусторонняя синхронизация с TMDB & Живой поиск",
        rm_02_d: "Мгновенный Omnibox-поиск любого фильма, сериала или аниме прямо на сайте. Полные карточки: актеры, фильмографии, бюджеты, рейтинги, кадры, трейлеры и факты. Двусторонняя синхронизация списков и каталогов в реальном времени.",
        rm_03_t: "Smart Subtitles & Изучение языка по кино",
        rm_03_d: "Двойные параллельные субтитры RU + EN. Мгновенный перевод любого незнакомого слова по клику или тапу прямо во время просмотра. Интерактивный личный словарь и сохранение вордлистов для прокачки английского по фильмам.",
        rm_04_t: "Свои субтитры (.srt/.vtt) & Skip Intro (TheIntroDB)",
        rm_04_d: "Возможность загрузить собственные файлы субтитров к любому тайтлу прямо в плеер. Автоматический пропуск опенингов и заставок сериалов в один клик через базу TheIntroDB без ручной перемотки.",
        rm_05_t: "Облачная библиотека & Точный синк до секунды",
        rm_05_d: "Умные закладки, папки («Буду смотреть», «Избранное»), история просмотров и функция «Продолжить просмотр» с точностью до секунды. Бесшовная кросс-девайс синхронизация между ПК, смартфоном и планшетом. Персональные AI-рекомендации.",
        rm_06_t: "AI-перевод субтитров на лету & Voice EQ",
        rm_06_d: "Мгновенная генерация и перевод субтитров нейросетями для свежайших мировых премьер, у которых еще нет официального дубляжа. Ночной режим нормализации звука: четкие диалоги поверх оглушающих спецэффектов.",
        rm_07_t: "Social Watch Party & Таймкод-шаринг моментов",
        rm_07_d: "Синхронный совместный просмотр фильмов и сериалов с друзьями по одной ссылке: единая перемотка, реакции и текстово-голосовой чат. Мгновенный шаринг любимых сцен с точным таймкодом и цитатами.",
        rm_08_t: "Семантический AI-поиск по вайбу & Мультипрофили",
        rm_08_d: "Умный подбор кино на естественном языке по настроению и скрытому смыслу («напряженный детектив в дождливом городе с неожиданным финалом»). Семейные изолированные профили с раздельной историей и рекомендациями.",
        rm_star_badge: "★ Ключевая цель экосистемы",
        rm_star_t: "Создать лучший стриминговый сервис и смести конкурентов",
        rm_star_d: "Объединить самую большую библиотеку кино в мире, адаптивный Multi-CDN плеер с мгновенным стартом, уникальные EdTech-фичи (Smart Subtitles, синхронизация с TMDB, TheIntroDB), нулевой рекламный шум и вирусную витрину сцен. Превзойти и устаревшие пиратские помойки с вирусами, и медленные легальные онлайн-кинотеатры с урезанными каталогами и платными подписками, сделав LightStream безальтернативным выбором для киноманов.",
        nav_07_moat: "Архитектурные рвы & Unit Economics",
        nav_08_road: "Timeline-роадмап фичей",
        nav_09_vel: "Shipping Velocity (Темп релизов)",
        nav_10_deals: "Форматы сотрудничества & M&A",
        moat_title: "Архитектурные рвы & Unit Economics",
        moat_desc: "Почему LightStream защищен от вытеснения: нулевые затраты на хранение видео, органический CAC $0 и высокий барьер удержания.",
        moat_hand_badge: "★ 88% Gross Margin Moat",
        moat_c1_t: "Zero-Storage Capex: Edge CDN Routing",
        moat_c1_d: "Классические OTT тратят миллионы на AWS S3 и транскодинг петабайт видео. LightStream балансирует между распределенными CDN-нодами и внешними стримами. Нулевой счет за хостинг видео при каталоге 100,000+ тайтлов.",
        moat_lbl_ott: "Классический OTT (AWS S3)",
        moat_val_ott_cost: "$120,000+ / мес",
        moat_val_ls_cost: "≈ $0 (Egress-neutral)",
        moat_c2_t: "Органический маховик & CAC = $0",
        moat_c2_d: "Нулевые затраты на платную рекламу. Привлечение через киноманские комьюнити, партизанский маркетинг в соцсетях, вирусные нарезки сцен и сарафанное радио за счет чистого плеера без скам-баннеров.",
        moat_lbl_market_cac: "Средний CAC в индустрии",
        moat_c3_t: "Барьер удержания: EdTech Lock-In",
        moat_c3_d: "Smart Subtitles с переводом по клику и личный словарь превращают развлечение в образовательный инструмент. Пользователь накапливает базу изученных слов и историю TMDB — уйти на другой сервис значит потерять прогресс.",
        moat_lbl_stickiness: "LTV мультипликатор",
        moat_lbl_churn: "Отток (Churn Rate)",
        moat_c4_t: "100% Иммунитет к AdBlock & SoV",
        moat_c4_d: "Интеграция спонсорства нативно на уровне платформы и плеера, без сторонних рекламных скриптов и фреймов, которые блокируются uBlock Origin и браузером Brave. Гарантированный 100% контакт с аудиторией.",
        moat_lbl_adblock_loss: "Потери трафика на сайтах (AdBlock)",
        vel_title: "Shipping Velocity: Реальный темп разработки",
        vel_desc: "Мы не пишем презентации месяцами — мы шипим боевой функционал каждую неделю. Журнал недавних релизов ядра LightStream:",
        vel_hand_badge: "★ Недельный релизный цикл",
        v_24_t: "Smart Subtitles & Двуязычный контекстный переводчик",
        v_24_d: "Интеграция пословного парсера WebVTT/SRT, всплывающие подсказки транскрипции и сохранение слов в персональный EdTech-словарь.",
        v_23_t: "TheIntroDB Интеграция & Skip Intro",
        v_23_d: "Автоматическое определение начала и конца заставок для сериалов и аниме по открытой краудсорс-базе таймкодов с пропуском в 1 клик.",
        v_22_t: "2-Way TMDB Sync & Быстрый Omnibox-поиск",
        v_22_d: "Двусторонняя синхронизация профилей с TMDB API (списки, закладки, оценки), дебаунс-поиск по десяткам тысяч актеров и фильмов.",
        v_21_t: "Multi-CDN Balancer & Переключение звуковых дорожек HLS",
        v_21_d: "Динамический failover между серверами отдачи, поддержка дорожек RHS, LostFilm, Кубик в Кубе и оригинального звука без задержек.",
        v_20_t: "Архитектура SvelteKit + Bun + Hono",
        v_20_d: "Полный рефакторинг фронтенда и API-шлюза: 0 рекламных фреймов, мгновенная загрузка страниц <400ms, безупречная адаптивность.",
        vel_ft_active: "Статус: Активная непрерывная разработка",
        memo_bar_title: "Executive Summary Memo (One-Pager)",
        memo_bar_sub: "Сформировать и скопировать готовый бриф в формате Markdown для отправки в Telegram или вставки в инвестиционные заметки.",
        memo_btn_txt: "Скопировать One-Pager Memo",
        memo_copied: "✓ Скопировано в буфер обмена для Telegram / Notion!",
        deal_title: "Форматы сотрудничества",
        deal_desc: "Прозрачные модели партнерства — от фиксированного рекламного ретейнера до полной продажи актива с передачей кода и инфраструктуры.",
        cta_title: "Обсудить партнерство или запросить доступ к метрикам",
        cta_desc: "Мы открыты к созвону в Google Meet или диалогу в Telegram для обсуждения фиксированной ставки спонсорства, параметров CPA-бейслайна или M&A аудита платформы.",
        cta_btn_tg: "Написать фаундеру: @shitmane ↗",
        cta_btn_app: "Открыть кинотеатр: lightstream.ws ↗"
      },
      en: {
        head_open_app: "Cinema App ↗",
        head_contact_tg: "Contact in TG",
        drawer_open_app: "Open lightstream.ws ↗",
        drawer_write_tg: "Contact Founder: @shitmane",
        menu_cat_offer: "OFFER & AUDIT",
        menu_cat_funnel: "FUNNEL & PRODUCT",
        nav_01: "Executive Brief & SoV",
        nav_02: "Key KPIs & Scale Stages",
        nav_03: "Verified 90-Day Analytics",
        nav_04: "Radar & Feature Matrix",
        nav_05: "Devices, GEO & Heatmap",
        nav_06: "Sponsor ROI Calculator",
        nav_07: "Timeline Feature Roadmap",
        nav_08: "Deal Models & M&A",
        aud_label: "Pitch Lens:",
        aud_sponsor: "Sponsors & Brands",
        aud_investor: "Investors & M&A",
        hero_status: "Status: Production (Month 2 Live) · Zero Third-Party Ads",
        hero_title_sponsor: "Next-Gen Web Cinema: 100% Monopoly Attention with Zero Ad Clutter",
        hero_sub_sponsor: "Zero spam pop-ups killed by AdBlock. Zero competing banners. LightStream gives 100% of our streaming video inventory to one exclusive partner with native ad-block bypass and 40+ minutes of focused attention per viewer.",
        hero_hand_note_sponsor: "42.5 min avg watch time (18x longer than social media)",
        hero_cta_tg_sponsor: "Book Exclusive via TG ↗",
        hero_title_investor: "Next-Gen Streaming Platform: CAC = $0, Compounding Organic Growth & Defensible Tech Moat",
        hero_sub_investor: "LightStream solves streaming's core bottleneck: delivers high-bitrate 1080p video with near-zero hosting burn, acquires viewers via viral autonomous distribution pipelines, and drives deep retention via EdTech subtitles and bidirectional TMDB sync.",
        hero_hand_note_investor: "★ Near-zero infrastructure burn + autonomous viral engine",
        hero_cta_tg_investor: "Request Data Room via TG ↗",
        hero_title: "Next-Gen Web Cinema: 100% Monopoly Attention with Zero Ad Clutter",
        hero_sub: "Zero spam pop-ups killed by AdBlock. Zero competing banners. LightStream gives 100% of our streaming video inventory to one exclusive betting/igaming partner with native ad-block bypass and 40+ minutes of focused attention per viewer.",
        hero_hand_note: "42.5 min avg watch time (18x longer than social media)",
        hero_cta_tg: "Book Exclusive via TG ↗",
        hero_cta_demo: "Open Live Cinema lightstream.ws ↗",
        hero_cta_memo: "Copy One-Pager Memo",
        hero_cta_scroll: "90-Day Metrics ↓",
        spec_app: "Platform",
        spec_stack: "Tech Stack",
        spec_noise: "Ad Clutter",
        spec_noise_val: "0 Third-Party Banners",
        spec_deal: "Deal Model",
        spec_deal_val: "100% Monopoly / M&A",
        pm_hand_note: "Interactive demo: tap a subtitle word or skip intro ↷",
        pm_tag_adblock: "0% AdBlock Detection",
        pm_btn_tmdb: "TMDB Info",
        pm_movie_name: "Oppenheimer (2023) · 4K Master",
        pm_skip_intro: "Skip Intro (01:42)",
        pm_pop_trans: "a major breakthrough or advance (noun)",
        pm_pop_save: "+ Save to Personal Vocabulary",
        pm_pop_saved: "✓ Saved to EdTech Vocabulary",
        pm_sub_before: "We are building a ",
        pm_sub_after: " streaming ecosystem for cinephiles.",
        pm_word_hint: "tap word",
        pm_tmdb_title: "TMDB Card (2-Way Sync)",
        pm_tmdb_dir_lbl: "Director:",
        pm_tmdb_cast_lbl: "Cast:",
        pm_tmdb_budget_lbl: "Budget:",
        pm_tmdb_sync_desc: "Bidirectional synchronization of watchlists and favorites with TMDB.",
        pm_tmdb_sync_btn: "+ Add to TMDB Watchlist",
        pm_tmdb_synced: "✓ Synced with TMDB API",
        kpi_title: "Key Metrics & Audience Scaling",
        kpi_desc: "Streaming inventory is measured in MAU and completed watch time. Toggle stage to review actual current metrics versus Q4 run-rate projections.",
        kpi_mau_label: "MAU (Monthly Active Users)",
        kpi_mau_note: "Organic cinephile user base",
        kpi_mau_hand: "★ 100% organic growth",
        kpi_session_label: "Average Watch Time",
        kpi_session_note: "18x longer than social feeds or pre-landers",
        kpi_session_hand: "★ deep continuous attention",
        kpi_views_label: "Monthly Video Plays",
        kpi_views_note: "100% clean plays in custom player",
        kpi_views_hand: "★ adaptive HLS engine",
        kpi_sov_label: "Share of Voice",
        kpi_sov_note: "Zero competing banners, zero clutter",
        kpi_sov_hand: "★ exclusive monopoly",
        ana_title: "Verified 90-Day Analytics Audit",
        ana_desc: "Real data from Plausible Analytics covering July 7 – October 3. Explosive organic adoption with zero paid ad spend.",
        ana_chart_title: "Viewership Growth Trend (90 Days)",
        ana_chart_sub: "Viral organic surge in September reaching >2,100 daily plays",
        stat_views: "Views",
        stat_sessions: "Sessions",
        stat_uniques: "Uniques",
        stat_duration: "Duration",
        radar_title: "Functional Radar: LightStream vs Netflix",
        radar_sub: "Benchmarking 6 core streaming and UX pillars",
        aud_title: "Devices, Browsers & Geographic Split",
        aud_desc: "Breakdown by viewer purchasing power, devices, and payment gateway compatibility.",
        aud_dev_title: "Viewer Devices & Browsers",
        aud_dev_sub: "Dominance of desktop and high-converting iOS traffic",
        aud_geo_title: "Verified Geographic Distribution",
        aud_geo_sub: "Split by countries, deposit power, and tier",
        prime_title: "Interactive Attention Heatmap & Prime-Time Matrix",
        prime_sub: "Click any time slot (days of week × hours) to inspect telemetry, session length, and Share of Voice.",
        prime_badge: "★ 19:00 – 23:30 Prime-Time (64% share)",
        heat_pre_prime: "★ Evening Prime-Time",
        heat_pre_lunch: "⚡ Wed 14:00 Lunch Spike",
        heat_pre_weekend: "🍿 Weekend Cinema",
        heat_pre_night: "🌙 Late Night Sessions",
        heat_pre_all: "🔄 Reset",
        heat_leg_title: "Activity:",
        heat_leg_peak: "Peak Airtime",
        heat_th_day: "Day",
        insp_gauge_lbl: "Engagement & Attention Index",
        insp_m_session: "Avg Session Length",
        insp_m_devices: "Large Screens",
        insp_m_sov: "Share of Voice",
        insp_m_retention: "AdBlock Bypass",
        prime_c1_tag: "Prime Window 19:00 – 23:30",
        prime_c1_val: "64% Daily Share",
        prime_c1_desc: "Peak attention period. Feature-length cinema viewing with average session duration exceeding 42 minutes.",
        prime_c2_tag: "Wednesday 14:00 Lunch Spike",
        prime_c2_val: "+45% Daytime Surge",
        prime_c2_desc: "Anomalous mid-week daytime surge driven by lunch-break viewing and short episodic series.",
        prime_c3_tag: "Desktop & Smart TV Dominance",
        prime_c3_val: "58% Large Screens",
        prime_c3_desc: "In evening hours viewers switch to full-screen mode, securing absolute 100% Share of Voice for partners.",
        calc_title: "Interactive Sponsor ROI Calculator",
        calc_desc: "Estimate direct returns from 100% Share of Voice on LightStream at target scale.",
        calc_lbl_mau: "Monthly Audience Reach (MAU)",
        calc_lbl_ctr: "Player CTR to Partner Offer",
        res_lbl_imp: "Video Impressions / mo",
        res_lbl_clk: "Direct Outbound Clicks",
        res_sub_adblock: "0% loss to AdBlock",
        res_lbl_ftd: "Projected FTDs (Deposits)",
        res_lbl_val: "Traffic Value (CPA Equiv.)",
        mat_title: "Technical Benchmark: Data instead of marketing",
        mat_desc: "Comparing LightStream's architecture with legacy streaming sites and Netflix.",
        th_feature: "Pillar / Feature",
        th_pirates: "Legacy Pirated Sites",
        road_title: "Feature Timeline Roadmap",
        road_desc: "Product expansion path: from core streaming engine to social watch parties and frontier AI search. No artificial calendar dates — strictly feature milestones.",
        road_hand_badge: "★ 01–08 Ecosystem Architecture",
        st_done: "Live In Prod ✓",
        st_wip: "In Progress ⚡",
        st_plan: "Planned",
        rm_01_t: "Largest Catalog & Multi-CDN Player Engine",
        rm_01_d: "Multi-CDN aggregation with instant failover, 1080p, and adaptive HLS/DASH streaming. All premier dubs and original audio tracks with zero player latency.",
        rm_02_t: "2-Way TMDB Sync & Instant Omnibox Search",
        rm_02_d: "Real-time search for any movie, TV series, or anime right on-site. Complete metadata: cast, filmographies, box office, ratings, stills, trailers, and trivia. Bidirectional TMDB list syncing.",
        rm_03_t: "Smart Bilingual Subtitles & Language Learning",
        rm_03_d: "Dual parallel subtitles (RU + EN). Click-to-translate any unknown word in real time during playback. Interactive vocabulary builder to master languages through cinema.",
        rm_04_t: "Custom Subtitles (.srt/.vtt) & Skip Intro (TheIntroDB)",
        rm_04_d: "Upload personal subtitle files directly into the player. One-tap automated skipping of TV series intros and title sequences powered by TheIntroDB.",
        rm_05_t: "Cloud Library & Second-Accurate Sync",
        rm_05_d: "Smart bookmarks, custom watchlists, viewing history, and second-accurate resume across desktop, mobile, and tablet. Personalized AI-driven discovery.",
        rm_06_t: "Live AI Subtitle Generation & Voice EQ",
        rm_06_d: "Instant neural transcription and translation for day-one global releases without official voiceovers. Night-mode voice clarifier balancing dialogue over explosions.",
        rm_07_t: "Social Watch Party & Timestamped Scene Sharing",
        rm_07_d: "Synchronized co-watching with friends via single shareable room link: synchronized scrubbing, live chat, and reactions. Instant sharing of iconic moments with exact timestamps.",
        rm_08_t: "Semantic AI Discovery & Isolated Multi-Profiles",
        rm_08_d: "Natural-language movie exploration by mood, aesthetics, and plot vibes. Dedicated multi-user household profiles with isolated histories.",
        rm_star_badge: "★ Ecosystem North Star",
        rm_star_t: "Build the Definitive Streaming Platform & Outclass Legacy Competitors",
        rm_star_d: "Unify the world's largest movie library, zero-buffer adaptive Multi-CDN engine, cutting-edge cinephile EdTech tools (Smart Subtitles, 2-way TMDB sync, TheIntroDB), zero intrusive ad clutter, and viral scene discovery. Outperforming both ad-infested legacy pirate sites and sluggish walled-garden OTT platforms with fragmented catalogs — making LightStream the uncontested default for cinema lovers.",
        nav_07_moat: "Defensive Moats & Unit Economics",
        nav_08_road: "Timeline Feature Roadmap",
        nav_09_vel: "Shipping Velocity & Git Log",
        nav_10_deals: "Deal Models & M&A",
        moat_title: "Defensive Moats & Unit Economics",
        moat_desc: "Structural defensibility: zero video hosting overhead, organic $0 CAC, and high retention switching costs.",
        moat_hand_badge: "★ 88% Gross Margin Moat",
        moat_c1_t: "Zero-Storage Capex: Edge CDN Routing",
        moat_c1_d: "Traditional OTT services burn millions on AWS S3 and transcode pipelines. LightStream balances across distributed CDN nodes and external streams. Zero video hosting bill across 100,000+ titles.",
        moat_lbl_ott: "Traditional OTT (AWS S3)",
        moat_val_ott_cost: "$120,000+ / mo",
        moat_val_ls_cost: "≈ $0 (Egress-neutral)",
        moat_c2_t: "Organic Flywheel & CAC = $0",
        moat_c2_d: "Zero paid user acquisition spend. Growth driven by cinema communities, guerrilla marketing on social platforms, viral clip highlights, and organic word-of-mouth thanks to a pristine ad-free player.",
        moat_lbl_market_cac: "Industry Average CAC",
        moat_c3_t: "Retention Moat: EdTech Lock-In",
        moat_c3_d: "Smart Subtitles with 1-tap translation and personal vocabulary transform entertainment into language learning. Users build up learned words and TMDB history — switching means losing progress.",
        moat_lbl_stickiness: "LTV Multiplier",
        moat_lbl_churn: "Churn Reduction",
        moat_c4_t: "100% AdBlock Immunity & 100% SoV",
        moat_c4_d: "Native first-party integration directly inside the player engine, with zero third-party ad scripts or tracking iframes that get killed by uBlock Origin or Brave browser.",
        moat_lbl_adblock_loss: "Standard Web Traffic Lost to AdBlock",
        vel_title: "Shipping Velocity: Production Track Record",
        vel_desc: "We don't spend months drafting slides — we ship production features every single week. Recent LightStream core release log:",
        vel_hand_badge: "★ Weekly Release Cadence",
        v_24_t: "Smart Subtitles & Contextual Vocab Engine",
        v_24_d: "Word-level WebVTT/SRT tokenization, phonetic popups, and instant 1-tap saving to personal EdTech vocabulary.",
        v_23_t: "TheIntroDB Integration & Skip Intro",
        v_23_d: "Automated intro & title sequence detection for series and anime via open-source timestamp database with 1-tap skip.",
        v_22_t: "2-Way TMDB Sync & Instant Omnibox Search",
        v_22_d: "Bidirectional watchlist and rating sync with official TMDB API, sub-millisecond debounced search across tens of thousands of films.",
        v_21_t: "Multi-CDN Balancer & HLS Audio Track Switcher",
        v_21_d: "Dynamic edge failover across streaming backends, latency-free audio switching between RHS, LostFilm, and original audio.",
        v_20_t: "SvelteKit + Bun + Hono Modern Architecture",
        v_20_d: "Complete frontend and gateway overhaul: 0 ad iframes, sub-400ms page loads, and responsive fluid layout.",
        vel_ft_active: "Status: Active Continuous Deployment",
        memo_bar_title: "Executive Summary Memo (One-Pager)",
        memo_bar_sub: "Generate and copy a concise, formatted Markdown brief ready for Telegram chats or VC investment memos.",
        memo_btn_txt: "Copy One-Pager Memo",
        memo_copied: "✓ Copied to clipboard for Telegram / Notion!",
        deal_title: "Deal Options & Cooperation Models",
        deal_desc: "Three transparent partnership paths — from exclusive monthly sponsorship to full asset acquisition.",
        cta_title: "Discuss Partnership or Request Analytics Access",
        cta_desc: "We are available for a Google Meet call or direct Telegram conversation to negotiate exclusive sponsorship, CPA parameters, or M&A audits.",
        cta_btn_tg: "Contact Founder: @shitmane ↗",
        cta_btn_app: "Open Cinema: lightstream.ws ↗"
      }
    };

    const dealsData = [
      {
        badge_ru: "★ 1 СЛОТ НА ПЛАТФОРМУ · 100% SoV",
        badge_en: "★ 1 SLOT EXCLUSIVE · 100% SoV",
        title_ru: "Генеральное спонсорство (100% Эксклюзив)",
        title_en: "Exclusive General Sponsorship (100% SoV)",
        sub_ru: "Полный монопольный выкуп видеоинвентаря платформы с фиксацией ставки до масштабирования",
        sub_en: "Fixed monthly retainer securing 100% video inventory across the platform",
        pts_ru: [
          "100% Share of Voice: ноль сторонних брендов, единственный партнер на платформе",
          "Интерактивный нативный видео-оверлей перед стартом и на паузе (0% потерь от AdBlock)",
          "★ Bonus Stack: брендирование в Telegram-сети + кликабельные карточки в каталоге TMDB",
          "★ Real-time телеметрия: прямой доступ к дашборду показов и посекундным досмотрам",
          "★ Risk Reversal: 7-дневный калибровочный пилот с гарантией фиксации CPM и объема показов",
          "★ Scarcity: Строго 1 генеральный партнер. При закрытии слота — включение в лист ожидания"
        ],
        pts_en: [
          "100% exclusive monopoly without a single competing brand on the entire platform",
          "Interactive native video overlay at start and on pause with 0% AdBlock drop-off",
          "★ Bonus Stack: branded Telegram network placement + clickable TMDB catalog cards",
          "★ Real-Time Telemetry: direct live access to impressions dashboard and watch-through rates",
          "★ Risk Reversal: 7-day calibration trial with guaranteed CPM rate lock & delivery baseline",
          "★ Scarcity: Strictly 1 general partner. Once reserved, subsequent advertisers enter waitlist"
        ],
        for_ru: "Крупные бренды, iGaming, Fintech, Web3 и прямые рекламодатели",
        for_en: "Top-tier brands, iGaming, Fintech, Web3, and direct advertisers"
      },
      {
        badge_ru: "Масштаб & Высокий LTV",
        badge_en: "Scale & High LTV",
        title_ru: "Эксклюзивный CPA / Hybrid с гарантией объема",
        title_en: "Exclusive CPA / Hybrid with Volume Baseline",
        sub_ru: "Высокая ставка за целевое действие + калиброванный нативный оверлей под киноманов",
        sub_en: "High CPA rate per conversion with calibrated player baseline",
        pts_ru: [
          "Персональный промокод и выделенный трекинг-домен под киноаудиторию",
          "Нативные триггерные кнопки («Смотри в 1080p Ultra с бонусом от партнера»)",
          "Раздельный роутинг по ГЕО (раздельные офферы под РФ, СНГ, Tier-1 Бурж)",
          "★ Bonus: контекстная интеграция промо-оффера в кликабельные EdTech-субтитры",
          "★ Risk Reversal: еженедельная сверка и прозрачные когорты удержания"
        ],
        pts_en: [
          "Dedicated tracking domain and promo codes tailored for cinephiles",
          "Custom native player CTA triggers («Stream in 1080p Ultra with partner bonus»)",
          "Granular GEO routing (split offers for CIS, US, Tier-1 Europe)",
          "★ Bonus: context-aware offer integration inside clickable EdTech subtitles",
          "★ Risk Reversal: weekly reconciliation with transparent retention cohorts"
        ],
        for_ru: "Партнерские сети и операторы с проверенным конверсионным воронком",
        for_en: "Affiliate networks and operators with battle-tested conversion funnels"
      },
      {
        badge_ru: "Strategic Round / M&A",
        badge_en: "Strategic Round / M&A",
        title_ru: "Инвестиции в масштаб / Полный выкуп актива (M&A)",
        title_en: "Scale Investment & Full Asset Buyout (M&A)",
        sub_ru: "Вход в капитал масштабируемого стриминга или выкуп готовой платформы под ключ",
        sub_en: "Equity entry into high-growth streaming platform or turnkey asset buyout",
        pts_ru: [
          "Полный стек: SvelteKit + Bun + Hono + HLS Multi-CDN видео-пайплайн",
          "Домен lightstream.ws + сетка автоматизированных каналов партизанского трафика",
          "Zero-Storage архитектура: околонулевой burn-rate на инфраструктуру ($0 capex на видео)",
          "★ Perspective: четкий роадмап масштабирования до 1,000,000+ MAU и вытеснения конкурентов",
          "★ Bonus: полное сопровождение интеграции от инженерной команды под ключ"
        ],
        pts_en: [
          "Full tech stack: SvelteKit + Bun + Hono + HLS Multi-CDN video pipeline",
          "Primary domain lightstream.ws + satellite viral organic acquisition channels",
          "Zero-Storage architecture: near-zero infrastructure burn-rate ($0 capex on video storage)",
          "★ Perspective: battle-tested roadmap to 1,000,000+ MAU disrupting legacy streaming giants",
          "★ Bonus: full engineering onboarding and integration handover by core team"
        ],
        for_ru: "Медиахолдинги, стратегические инвесторы и экосистемы, строящие свой OTT-стриминг",
        for_en: "Media conglomerates, strategic investors, and OTT ecosystems"
      }
    ];

    function renderDeals(lang) {
      const container = document.getElementById('dealsContainer');
      if (!container) return;
      container.innerHTML = '';

      dealsData.forEach((d, idx) => {
        const card = document.createElement('div');
        card.className = 'sketch-card deal-card' + (idx === 0 ? ' primary' : '');
        const badge = lang === 'ru' ? d.badge_ru : d.badge_en;
        const title = lang === 'ru' ? d.title_ru : d.title_en;
        const sub = lang === 'ru' ? d.sub_ru : d.sub_en;
        const pts = lang === 'ru' ? d.pts_ru : d.pts_en;
        const forWhom = lang === 'ru' ? d.for_ru : d.for_en;

        const ptsHtml = pts.map(p => `<li>${p}</li>`).join('');
        card.innerHTML = `
          <div>
            <span class="deal-badge">${badge}</span>
            <h3 class="deal-title">${title}</h3>
            <p class="deal-sub">${sub}</p>
            <ul class="deal-pts">${ptsHtml}</ul>
          </div>
          <div class="deal-footer">
            ${lang === 'ru' ? 'Кому подходит:' : 'Target:'} <strong>${forWhom}</strong>
          </div>
        `;
        container.appendChild(card);
      });
    }

    // Step 2: Interactive Heatmap Matrix & Inspector Engine
    const heatSlotProfiles = {
      'wed-20': {
        title_ru: 'Среда · 20:00 – 22:00',
        title_en: 'Wednesday · 20:00 – 22:00',
        status_ru: '★ Абсолютный пик недели (Киносеанс)',
        status_en: '★ All-Time Weekly Peak (Cinema Prime)',
        tag: '100% SoV',
        idx: 100,
        session: '48.5 мин',
        devices: '64% Smart TV & PC',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Золотое окно полного внимания. Пользователи смотрят полнометражные премьеры на больших экранах без перемотки. Премиальный слот для монопольного брендинга и нативных pre-roll вставок без потерь от блокировщиков.»',
        desc_en: '“Golden prime attention slot. Cinephiles stream full-length premieres on big screens without skips. Monopoly sponsor real-estate with zero AdBlock drop-off.”'
      },
      'wed-14': {
        title_ru: 'Среда · 14:00 (Lunch Spike)',
        title_en: 'Wednesday · 14:00 (Lunch Spike)',
        status_ru: '⚡ Дневной аномальный пик (+45%)',
        status_en: '⚡ Daytime Viral Surge (+45%)',
        tag: 'High CTR',
        idx: 94,
        session: '28.2 мин',
        devices: '54% Mobile, 46% PC',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Обеденный тайм-аут: фоновые сериалы и короткометражки в офисах и на смартфонах. Самый высокий показатель CTR на единицу времени среди дневных слотов.»',
        desc_en: '“Midday lunch break anomaly: episodic streaming and short viewing sessions across mobile and desktop. Highest daytime click-through intent.”'
      },
      'fri-20': {
        title_ru: 'Пятница · 20:00 – 23:30',
        title_en: 'Friday · 20:00 – 23:30',
        status_ru: '🍿 Старт уикенда (Ночной кинозал)',
        status_en: '🍿 Weekend Kickoff (Late Night Cinema)',
        tag: 'Max Duration',
        idx: 97,
        session: '54.0 мин',
        devices: '71% Smart TV & PC',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Рекордная средняя продолжительность одного сеанса (54 мин). Парный и семейный просмотр в высоком битрейте 1080p Ultra. Максимальная запоминаемость спонсорского посыла.»',
        desc_en: '“Highest single-session watch duration (54 min avg). Living room and family viewing in 1080p Ultra adaptive bitrate. Maximum sponsor brand recall.”'
      },
      'sat-20': {
        title_ru: 'Суббота · 20:00 – 22:30',
        title_en: 'Saturday · 20:00 – 22:30',
        status_ru: '🎬 Семейный прайм-кинозал',
        status_en: '🎬 Family Prime Cinema Evening',
        tag: 'Co-Viewing',
        idx: 98,
        session: '52.4 мин',
        devices: '73% Smart TV',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Пиковый охват домашних экранов. 73% аудитории смотрят через браузер Smart TV / HDMI, обеспечивая эффект со-смотрения (в среднем 2.3 зрителя на экран).»',
        desc_en: '“Peak living room reach. 73% big-screen viewing delivering natural co-viewing multipliers (avg 2.3 persons per screen).”'
      },
      'sun-20': {
        title_ru: 'Воскресенье · 20:00 – 22:00',
        title_en: 'Sunday · 20:00 – 22:00',
        status_ru: '☕ Финал уикенда (Досмотры)',
        status_en: '☕ Weekend Finale (Catch-up Sessions)',
        tag: 'High Focus',
        idx: 96,
        session: '46.8 мин',
        devices: '62% Smart TV & PC',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Вдумчивые просмотры авторского кино и финалов сезонов сериалов перед рабочей неделей. Высокое вовлечение и отсутствие оттока.»',
        desc_en: '“Deep dive into season finales and cinephile picks before the workweek starts. Low bounce rate, premium viewer engagement.”'
      },
      'night': {
        title_ru: 'Ночной слот · 00:00 – 04:00',
        title_en: 'Night Slot · 00:00 – 04:00',
        status_ru: '🌙 Фоновый ночной стриминг (8%)',
        status_en: '🌙 Late Night Background Streaming (8%)',
        tag: 'Niche Tech',
        idx: 32,
        session: '38.0 мин',
        devices: '68% Desktop (IT/Devs)',
        sov: '100% Exclusive',
        adblock: '100% Доставка',
        desc_ru: '«Ядро ночной аудитории — программисты, дизайнеры и ночные киноманы. Превосходный таргетинг для IT-продуктов, крипто-сервисов и edtech.»',
        desc_en: '“Core night audience: developers, creatives and nocturnal cinephiles. Precision targeting for developer tools, Web3, and EdTech.”'
      }
    };

    const dayNames = {
      ru: { mon: 'Понедельник', tue: 'Вторник', wed: 'Среда', thu: 'Четверг', fri: 'Пятница', sat: 'Суббота', sun: 'Воскресенье' },
      en: { mon: 'Monday', tue: 'Tuesday', wed: 'Wednesday', thu: 'Thursday', fri: 'Friday', sat: 'Saturday', sun: 'Sunday' }
    };

    let activeHeatKey = 'wed-20';

    function updateHeatInspector(key, dayKey = 'wed', hour = '20', idx = '100') {
      activeHeatKey = key;
      const lang = currentLang;
      const prof = heatSlotProfiles[key];
      const titleEl = document.getElementById('inspSlotTitle');
      const statusEl = document.getElementById('inspSlotStatus');
      const tagEl = document.getElementById('inspTagSlot');
      const idxEl = document.getElementById('inspIdxVal');
      const gaugeFill = document.getElementById('inspGaugeFill');
      const sessionEl = document.getElementById('inspSessionVal');
      const devEl = document.getElementById('inspDeviceVal');
      const sovEl = document.getElementById('inspSovVal');
      const adbEl = document.getElementById('inspAdblockVal');
      const descEl = document.getElementById('inspDesc');

      if (prof) {
        if (titleEl) titleEl.textContent = lang === 'ru' ? prof.title_ru : prof.title_en;
        if (statusEl) statusEl.textContent = lang === 'ru' ? prof.status_ru : prof.status_en;
        if (tagEl) tagEl.textContent = prof.tag;
        if (idxEl) idxEl.textContent = `${prof.idx} / 100`;
        if (gaugeFill) gaugeFill.style.width = `${prof.idx}%`;
        if (sessionEl) sessionEl.textContent = prof.session;
        if (devEl) devEl.textContent = prof.devices;
        if (sovEl) sovEl.textContent = prof.sov;
        if (adbEl) adbEl.textContent = prof.adblock;
        if (descEl) descEl.textContent = lang === 'ru' ? prof.desc_ru : prof.desc_en;
      } else {
        const dName = (dayNames[lang] && dayNames[lang][dayKey]) || dayKey;
        const hNum = parseInt(hour, 10);
        const hEnd = (hNum + 2) % 24;
        const hStr = `${String(hNum).padStart(2,'0')}:00 – ${String(hEnd).padStart(2,'0')}:00`;
        const isPrime = hNum >= 18 && hNum <= 22;
        const valIdx = parseInt(idx, 10) || 40;

        if (titleEl) titleEl.textContent = `${dName} · ${hStr}`;
        if (statusEl) statusEl.textContent = isPrime 
          ? (lang === 'ru' ? '🎬 Вечерний кинозал (Prime-Time)' : '🎬 Prime-Time Cinema Slot')
          : (lang === 'ru' ? 'Телеметрия слота' : 'Slot Telemetry');
        if (tagEl) tagEl.textContent = isPrime ? '100% SoV' : 'Active';
        if (idxEl) idxEl.textContent = `${valIdx} / 100`;
        if (gaugeFill) gaugeFill.style.width = `${valIdx}%`;
        if (sessionEl) sessionEl.textContent = isPrime ? '44.2 мин' : `${Math.round(20 + valIdx * 0.25)} мин`;
        if (devEl) devEl.textContent = isPrime ? '60% Smart TV & PC' : '48% Desktop, 52% Mobile';
        if (sovEl) sovEl.textContent = '100% Exclusive';
        if (adbEl) adbEl.textContent = '100% Доставка';
        if (descEl) descEl.textContent = isPrime
          ? (lang === 'ru' ? '«Вечерний сеанс. Высокое удержание аудитории, непрерывный просмотр фильмов в 1080p без баннерного шума.»' : '“Evening session. High engagement rate, uninterrupted 1080p movie streaming with zero banner fatigue.”')
          : (lang === 'ru' ? '«Регулярный трафик кинотеатра. Плеер обеспечивает 100% доставку спонсорского контента мимо всех блокировщиков рекламы.»' : '“Standard platform traffic. Proprietary player delivers 100% sponsor creative bypassing all adblockers.”');
      }
    }

    function initHeatmapEvents() {
      const cells = document.querySelectorAll('.heat-cell');
      cells.forEach(cell => {
        cell.addEventListener('click', () => {
          cells.forEach(c => c.classList.remove('is-selected'));
          cell.classList.add('is-selected');
          const d = cell.dataset.d;
          const h = cell.dataset.h;
          const idx = cell.dataset.idx;
          const key = `${d}-${h}`;
          updateHeatInspector(key, d, h, idx);
        });
        cell.addEventListener('mouseenter', () => {
          const d = cell.dataset.d;
          const h = cell.dataset.h;
          const idx = cell.dataset.idx;
          const key = `${d}-${h}`;
          updateHeatInspector(key, d, h, idx);
        });
      });
    }

    function applyHeatPreset(type) {
      document.querySelectorAll('.heat-preset-btn').forEach(b => b.classList.remove('active'));
      const activeBtn = document.getElementById(type === 'prime' ? 'presetPrime' : type === 'lunch' ? 'presetLunch' : type === 'weekend' ? 'presetWeekend' : type === 'night' ? 'presetNight' : 'presetAll');
      if (activeBtn) activeBtn.classList.add('active');

      const cells = document.querySelectorAll('.heat-cell');
      cells.forEach(c => {
        c.classList.remove('is-selected');
        c.style.outline = '';
      });

      if (type === 'prime') {
        const primeCells = document.querySelectorAll('.heat-cell[data-h="18"], .heat-cell[data-h="20"], .heat-cell[data-h="22"]');
        primeCells.forEach(c => c.style.outline = '1px solid rgba(255,255,255,0.4)');
        setTimeout(() => primeCells.forEach(c => c.style.outline = ''), 1500);
        const sel = document.querySelector('.heat-cell[data-d="wed"][data-h="20"]');
        if (sel) sel.classList.add('is-selected');
        updateHeatInspector('wed-20', 'wed', '20', '100');
      } else if (type === 'lunch') {
        const sel = document.querySelector('.heat-cell[data-d="wed"][data-h="14"]');
        if (sel) sel.classList.add('is-selected');
        updateHeatInspector('wed-14', 'wed', '14', '94');
      } else if (type === 'weekend') {
        const sel = document.querySelector('.heat-cell[data-d="fri"][data-h="20"]');
        if (sel) sel.classList.add('is-selected');
        updateHeatInspector('fri-20', 'fri', '20', '97');
      } else if (type === 'night') {
        const sel = document.querySelector('.heat-cell[data-d="wed"][data-h="0"]');
        if (sel) sel.classList.add('is-selected');
        updateHeatInspector('night', 'wed', '0', '32');
      } else {
        const sel = document.querySelector('.heat-cell[data-d="wed"][data-h="20"]');
        if (sel) sel.classList.add('is-selected');
        updateHeatInspector('wed-20', 'wed', '20', '100');
      }
    }

    // Step 5: One-Click Executive Memo Copy Handler
    function copyExecutiveMemo() {
      const isSponsor = currentAudience === 'sponsor';
      const isRu = currentLang === 'ru';
      let memoText = '';

      if (isRu) {
        if (isSponsor) {
          memoText = '# LightStream (lightstream.ws) — Спонсорский & Бренд Оффер\\n' +
            '• Платформа: Стриминговый кинотеатр нового поколения без баннерного шума (https://lightstream.ws)\\n' +
            '• Охват & Удержание: 120,000 MAU | 850,000 запусков видео/мес | Средняя сессия: 42.5 минуты\\n' +
            '• Формат: 100% монопольный Share of Voice, нативная интеграция в плеер, 0% потерь от AdBlock / Brave\\n' +
            '• Профиль аудитории: 21–38 лет, платежеспособная, гики, киноманы, IT-специалисты (72% Desktop & Smart TV)\\n' +
            '• Онлайн-питч & Метрики: https://wdnameless.github.io/lightstream-pitch/\\n' +
            '• Контакт для бронирования: Telegram @shitmane | Email: good22067@gmail.com';
        } else {
          memoText = '# LightStream (lightstream.ws) — Executive Investment & M&A Memo\\n' +
            '• Продукт: Независимый видеостриминговый сервис с каталогом 100,000+ тайтлов (SvelteKit · Bun · Hono · HLS)\\n' +
            '• Текущие метрики: 120,000 MAU | 42.5 мин средняя сессия | CAC = $0 (100% органический рост)\\n' +
            '• Архитектурный ров: Нулевой Capex на видео (мульти-CDN edge роутинг), EdTech-удержание (Smart Subtitles + TMDB sync)\\n' +
            '• Монетизация & Выход: 88% Gross Margin на монопольном спонсорстве + высокий потенциал M&A поглощения\\n' +
            '• Инвесторский питч: https://wdnameless.github.io/lightstream-pitch/\\n' +
            '• Прямой контакт фаундера: Telegram @shitmane | Email: good22067@gmail.com';
        }
      } else {
        if (isSponsor) {
          memoText = '# LightStream (lightstream.ws) — Executive Sponsorship One-Pager\\n' +
            '• Platform: Next-gen streaming ecosystem with zero banner clutter (https://lightstream.ws)\\n' +
            '• Scale & Retention: 120,000 MAU | 850,000 monthly video plays | 42.5 min average watch session\\n' +
            '• Inventory Format: 100% Monopoly Share of Voice, native in-player delivery, 0% AdBlock script loss\\n' +
            '• Audience Profile: 21–38 tech-savvy cinephiles (72% Desktop & Smart TV, high disposable income)\\n' +
            '• Live Pitch & Telemetry: https://wdnameless.github.io/lightstream-pitch/?lang=en\\n' +
            '• Direct Booking: Telegram @shitmane | Email: good22067@gmail.com';
        } else {
          memoText = '# LightStream (lightstream.ws) — Executive Investment & M&A One-Pager\\n' +
            '• Product: Independent high-velocity streaming platform with 100,000+ catalog (SvelteKit · Bun · Hono · HLS)\\n' +
            '• Traction & Unit Economics: 120,000 MAU | 42.5 min session duration | CAC = $0.00 (100% organic flywheel)\\n' +
            '• Core Moat: Zero-storage Capex (multi-CDN stream balancing), EdTech retention lock-in (Smart Subtitles + TMDB sync)\\n' +
            '• Economics & Exit: 88% Gross Margin on exclusive brand inventory + high M&A buyout appeal for OTT ecosystems\\n' +
            '• Pitch Deck: https://wdnameless.github.io/lightstream-pitch/?lang=en\\n' +
            '• Founder Direct: Telegram @shitmane | Email: good22067@gmail.com';
        }
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(memoText).then(showToast).catch(() => fallbackCopy(memoText));
      } else {
        fallbackCopy(memoText);
      }
    }

    function fallbackCopy(text) {
      const ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.focus();
      ta.select();
      try { document.execCommand('copy'); showToast(); } catch(e){}
      document.body.removeChild(ta);
    }

    let toastTimer = null;
    function showToast() {
      const toast = document.getElementById('memoToast');
      if (!toast) return;
      const dict = i18nData[currentLang];
      const toastText = document.getElementById('memoToastText');
      if (toastText) toastText.textContent = dict.memo_copied || (currentLang === 'ru' ? '✓ Скопировано в буфер обмена для Telegram / Notion!' : '✓ Copied to clipboard for Telegram / Notion!');
      toast.classList.add('show');
      if (toastTimer) clearTimeout(toastTimer);
      toastTimer = setTimeout(() => {
        toast.classList.remove('show');
      }, 3500);
    }

    init();
  </script>

  <!-- Step 5: Floating Toast Notification for Executive Memo -->
  <div id="memoToast" class="toast-memo">
    <span>✓</span>
    <span id="memoToastText" data-i18n="memo_copied">Скопировано в буфер обмена для Telegram / Notion!</span>
  </div>
</body>
</html>
'''

output_path = r"D:\lightstream\pitch-site\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully compiled hand-drawn blueprint pitch deck to {output_path}! File size: {os.path.getsize(output_path)} bytes")

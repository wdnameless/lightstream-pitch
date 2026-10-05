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

    .hero-eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 4px 12px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      margin-bottom: 24px;
      font-family: var(--mono);
      font-size: 11px;
      color: var(--text-muted);
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

    /* Punchcard Heatmap */
    .punchcard-wrap {
      padding: 24px;
      margin-bottom: 24px;
      overflow: hidden;
    }

    .punchcard-scroll {
      width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      padding-bottom: 6px;
    }

    .punchcard-table {
      min-width: 580px;
      width: 100%;
      border-collapse: collapse;
      font-family: var(--mono);
      font-size: 11px;
    }

    .punchcard-table th {
      padding: 6px;
      color: var(--text-dim);
      font-weight: 500;
      text-align: center;
    }

    .punchcard-table td {
      padding: 8px 6px;
      text-align: center;
    }

    .p-day {
      text-align: left !important;
      color: var(--text-muted);
      font-weight: 600;
      width: 50px;
    }

    .p-dot {
      display: inline-block;
      border-radius: 50%;
      background: #fafafa;
      transition: all 0.15s ease;
    }

    .p-dot:hover {
      transform: scale(1.4);
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
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

    .t-badge {
      font-family: var(--mono);
      font-size: 10px;
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      font-weight: 600;
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
      padding-top: 24px;
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
      <a href="#benchmark" class="drawer-link" data-close>
        <span><span class="num">04</span> <span data-i18n="nav_04">Радар & Матрица vs Netflix</span></span>
        <span class="tag">7 / 9</span>
      </a>

      <div class="drawer-category" data-i18n="menu_cat_funnel">ВОРОНКА И ПРОДУКТ</div>
      <a href="#audience" class="drawer-link" data-close>
        <span><span class="num">05</span> <span data-i18n="nav_05">Устройства, ГЕО и Прайм-тайм</span></span>
        <span class="tag">Audience</span>
      </a>
      <a href="#calculator" class="drawer-link" data-close>
        <span><span class="num">06</span> <span data-i18n="nav_06">Калькулятор отдачи (ROI)</span></span>
        <span class="tag">FTD Calc</span>
      </a>
      <a href="#roadmap" class="drawer-link" data-close>
        <span><span class="num">07</span> <span data-i18n="nav_07">Timeline-роадмап фичей</span></span>
        <span class="tag">Arrow</span>
      </a>
      <a href="#deals" class="drawer-link" data-close>
        <span><span class="num">08</span> <span data-i18n="nav_08">Форматы сотрудничества & M&A</span></span>
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
      <div class="hero-eyebrow">
        <span class="pulse-dot"></span>
        <span data-i18n="hero_status">Статус: Production (2 месяца в проде) · 0 сторонней рекламы</span>
      </div>

      <h1 data-i18n="hero_title">
        Браузерный кинотеатр без рекламного спама: 100% Share of Voice для одного прямого спонсора
      </h1>

      <p class="hero-sub" data-i18n="hero_sub">
        Мы не продаем спам-клики на пиратских сайтах с 15 поп-апами, которые срезает AdBlock. 
        LightStream отдает весь видеоинвентарь <strong>одной гемблинг или беттинг сетке</strong> на условиях монополии, нативного обхода блокировщиков и 40+ минут внимания на каждого зрителя.
      </p>

      <!-- Handcrafted Annotation Callout with Sketch Arrow -->
      <div class="hero-callout-row">
        <div class="sketch-arrow-wrap">
          <svg viewBox="0 0 60 30">
            <path d="M 50,5 Q 25,25 5,15" />
            <polyline points="15,8 5,15 12,24" />
          </svg>
          <span data-i18n="hero_hand_note">42.5 мин средний просмотр (в 18 раз дольше соцсетей)</span>
        </div>
      </div>

      <!-- Action Funnel Buttons -->
      <div class="hero-cta-group">
        <a href="https://t.me/shitmane" target="_blank" rel="noopener" class="btn btn-primary" style="padding:11px 22px; font-size:14px;">
          <span data-i18n="hero_cta_tg">Забронировать эксклюзив в TG ↗</span>
        </a>
        <a href="https://lightstream.ws" target="_blank" rel="noopener" class="btn btn-secondary" style="padding:11px 22px; font-size:14px;">
          <span data-i18n="hero_cta_demo">Открыть кинотеатр lightstream.ws ↗</span>
        </a>
        <a href="#analytics" class="btn btn-secondary" style="padding:11px 18px; font-size:13px; font-family:var(--mono);">
          <span data-i18n="hero_cta_scroll">Метрики 90д ↓</span>
        </a>
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

    <!-- Section 1: Executive KPI Cards & Projections -->
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

      <div class="infographics-grid">
        <!-- Chart 1: Traffic dynamics (Blueprint Handcrafted SVG) -->
        <div class="sketch-card chart-card">
          <div class="chart-card-header">
            <div>
              <div class="chart-card-title" data-i18n="ana_chart_title">Динамика просмотров (7 июл – 3 окт)</div>
              <div class="chart-card-sub" data-i18n="ana_chart_sub">Органический взлет в сентябре с пиком >2,100 просмотров/сутки</div>
            </div>
            <span class="hand-badge" style="color:var(--accent-green); border-color:#064e3b;">+100% Growth</span>
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

        <!-- Chart 2: Radar matrix (LightStream 7/9 vs Netflix 2/9) -->
        <div class="sketch-card chart-card" id="benchmark">
          <div class="chart-card-header">
            <div>
              <div class="chart-card-title" data-i18n="radar_title">Радар функционала: LightStream vs Netflix</div>
              <div class="chart-card-sub" data-i18n="radar_sub">Сравнение по 6 ключевым осям стриминга и технологий</div>
            </div>
            <span class="hand-badge" style="color:#fafafa; border-color:#525363;">7 / 9 фич</span>
          </div>

          <div class="radar-svg-box">
            <svg viewBox="0 0 380 270" width="100%" height="100%">
              <!-- Rings -->
              <polygon points="190,38 272,86 272,180 190,228 108,180 108,86" fill="none" stroke="#252632" stroke-width="1.5" stroke-dasharray="3 3"/>
              <polygon points="190,70 245,101 245,165 190,196 135,165 135,101" fill="none" stroke="#1f202b" stroke-width="1"/>
              <polygon points="190,102 218,118 218,150 190,166 162,150 162,118" fill="none" stroke="#171822" stroke-width="1"/>

              <!-- Axes -->
              <line x1="190" y1="134" x2="190" y2="38" stroke="#252632" stroke-width="1"/>
              <line x1="190" y1="134" x2="272" y2="86" stroke="#252632" stroke-width="1"/>
              <line x1="190" y1="134" x2="272" y2="180" stroke="#252632" stroke-width="1"/>
              <line x1="190" y1="134" x2="190" y2="228" stroke="#252632" stroke-width="1"/>
              <line x1="190" y1="134" x2="108" y2="180" stroke="#252632" stroke-width="1"/>
              <line x1="190" y1="134" x2="108" y2="86" stroke="#252632" stroke-width="1"/>

              <!-- Netflix Polygon -->
              <polygon points="190,55 246,101 210,146 190,154 128,168 128,99" 
                       fill="rgba(239, 68, 68, 0.12)" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="4 3"/>

              <!-- LightStream Polygon -->
              <polygon points="190,42 268,89 264,176 190,216 112,177 112,89" 
                       fill="rgba(250, 250, 250, 0.22)" stroke="#fafafa" stroke-width="2.2"/>
              <circle cx="190" cy="42" r="3.5" fill="#fafafa"/>
              <circle cx="268" cy="89" r="3.5" fill="#fafafa"/>
              <circle cx="264" cy="176" r="3.5" fill="#fafafa"/>
              <circle cx="190" cy="216" r="3.5" fill="#fafafa"/>
              <circle cx="112" cy="177" r="3.5" fill="#fafafa"/>
              <circle cx="112" cy="89" r="3.5" fill="#fafafa"/>

              <!-- Labels -->
              <text x="190" y="24" fill="#fafafa" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Библиотека (TMDB)</text>
              <text x="282" y="87" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="start">Плеер (UX)</text>
              <text x="280" y="184" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="start">Интеграции</text>
              <text x="190" y="252" fill="#fafafa" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Аудио / Voice</text>
              <text x="98" y="184" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">Субтитры (RU+EN)</text>
              <text x="98" y="87" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">ИИ-поиск</text>
            </svg>
          </div>

          <div class="radar-legend">
            <div class="legend-tag">
              <span class="legend-color-box" style="background:#fafafa; box-shadow:0 0 8px rgba(255,255,255,0.6);"></span>
              <span><strong>LightStream</strong> (7/9 фич, 100% SoV)</span>
            </div>
            <div class="legend-tag">
              <span class="legend-color-box" style="background:#ef4444;"></span>
              <span style="color:#ef4444;">Netflix (2/9 фич)</span>
            </div>
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

      <!-- Traffic Punchcard Heatmap -->
      <div class="sketch-card punchcard-wrap">
        <div class="chart-card-header">
          <div>
            <div class="chart-card-title" data-i18n="punch_title">Тепловая карта активности (Punchcard Heatmap)</div>
            <div class="chart-card-sub" data-i18n="punch_sub">Пик внимания: среда 14:00+ и вечерние сеансы 19:00–23:00</div>
          </div>
          <span class="hand-badge" style="color:var(--accent-green); border-color:#064e3b;">Prime-Time</span>
        </div>

        <div class="punchcard-scroll">
          <table class="punchcard-table">
            <thead>
              <tr>
                <th class="p-day">День</th>
                <th>00ч</th><th>03ч</th><th>06ч</th><th>09ч</th><th>12ч</th>
                <th>14ч ★</th><th>16ч</th><th>18ч</th><th>20ч</th><th>22ч</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="p-day">Вс</td>
                <td><span class="p-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="p-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:4px; height:4px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="p-dot" style="width:10px; height:10px; opacity:0.7;"></span></td>
                <td><span class="p-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
              </tr>
              <tr>
                <td class="p-day">Пн</td>
                <td><span class="p-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="p-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="p-dot" style="width:10px; height:10px; opacity:0.7;"></span></td>
                <td><span class="p-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="p-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
              </tr>
              <tr>
                <td class="p-day">Вт</td>
                <td><span class="p-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="p-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="p-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
              <tr style="background: rgba(255,255,255,0.03);">
                <td class="p-day" style="color:#fafafa;">Ср ★</td>
                <td><span class="p-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="p-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="p-dot" style="width:3px; height:3px; opacity:0.25;"></span></td>
                <td><span class="p-dot" style="width:7px; height:7px; opacity:0.5;"></span></td>
                <td><span class="p-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="p-dot" style="width:18px; height:18px; opacity:1.0; box-shadow:0 0 12px rgba(255,255,255,0.8);"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:17px; height:17px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
              </tr>
              <tr>
                <td class="p-day">Чт</td>
                <td><span class="p-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="p-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="p-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
              <tr>
                <td class="p-day">Пт</td>
                <td><span class="p-dot" style="width:7px; height:7px; opacity:0.55;"></span></td>
                <td><span class="p-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="p-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:17px; height:17px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
              </tr>
              <tr>
                <td class="p-day">Сб</td>
                <td><span class="p-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="p-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="p-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="p-dot" style="width:4px; height:4px; opacity:0.3;"></span></td>
                <td><span class="p-dot" style="width:9px; height:9px; opacity:0.65;"></span></td>
                <td><span class="p-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="p-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="p-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="p-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="p-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
            </tbody>
          </table>
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

    <!-- Section 5: Comparison Matrix -->
    <section class="section" id="matrix">
      <div class="section-header">
        <div>
          <h2 class="section-title" data-i18n="mat_title">Сравнение стека: Data instead of marketing</h2>
          <p class="section-desc" data-i18n="mat_desc">
            Технологические возможности LightStream против устаревших пиратских плееров и Netflix.
          </p>
        </div>
        <span class="hand-badge" style="color:var(--accent-green); border-color:#064e3b;">LightStream: 7/9 фич</span>
      </div>

      <div class="sketch-card matrix-box">
        <table class="matrix-tbl">
          <thead>
            <tr>
              <th style="width: 32%;" data-i18n="th_feature">Критерий / Фича</th>
              <th style="width: 17%;">LightStream</th>
              <th style="width: 17%;">Netflix</th>
              <th style="width: 17%;">Кинопоиск</th>
              <th style="width: 17%;" data-i18n="th_pirates">Пиратские сайты</th>
            </tr>
          </thead>
          <tbody id="matrixBody">
            <!-- Rendered by JS based on language -->
          </tbody>
        </table>
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
        <span class="hand-badge">Timeline Arrow</span>
      </div>

      <div class="timeline-wrap">
        <div class="timeline-stem"></div>

        <!-- 01: Core Player (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-done">01</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#064e3b; color:#34d399;" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Core Engine</span>
            </div>
            <div class="t-title" data-i18n="rm_01_t">HLS/DASH Адаптивный видеодвижок</div>
            <div class="t-desc" data-i18n="rm_01_d">
              Мульти-CDN агрегация с автопереключением источников, 1080p, мгновенная буферизация и uBlock-обход за счет нативного рендеринга.
            </div>
          </div>
        </div>

        <!-- 02: SEO & Agentic TMDB (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-done">02</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#064e3b; color:#34d399;" data-i18n="st_done">В проде ✓</span>
              <span class="t-stage">Growth Pipeline</span>
            </div>
            <div class="t-title" data-i18n="rm_02_t">SEO Оптимизация & Agentic TMDB-синк</div>
            <div class="t-desc" data-i18n="rm_02_d">
              Автоматическая генерация тайтл-карточек, актерских страниц, трейлеров и рейтингов. Быстрая индексация поисковиками и чистая органика.
            </div>
          </div>
        </div>

        <!-- 03: Threads & Telegram Viral Machine (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-wip">03</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#1e3a8a; color:#60a5fa;" data-i18n="st_wip">В работе ⚡</span>
              <span class="t-stage">Viral Distribution</span>
            </div>
            <div class="t-title" data-i18n="rm_03_t">Threads & Telegram вирусный трафик</div>
            <div class="t-desc" data-i18n="rm_03_d">
              Автоматизированная фабрика синефильских нарезок и трейлеров. Партизанский маркетинг, привлекающий зрителей с CAC = $0.
            </div>
          </div>
        </div>

        <!-- 04: Asian Dramas (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-wip">04</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#1e3a8a; color:#60a5fa;" data-i18n="st_wip">В работе ⚡</span>
              <span class="t-stage">Content Expansion</span>
            </div>
            <div class="t-title" data-i18n="rm_04_t">Хаб азиатского контента («Дорамы»)</div>
            <div class="t-desc" data-i18n="rm_04_d">
              Выделенные рельсы и подборки корейских и китайских сериалов с высочайшим retention, глубиной досмотра и повторными визитами.
            </div>
          </div>
        </div>

        <!-- 05: Google One-Tap & Cloud Aliases (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-wip">05</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#1e3a8a; color:#60a5fa;" data-i18n="st_wip">В работе ⚡</span>
              <span class="t-stage">User Identity</span>
            </div>
            <div class="t-title" data-i18n="rm_05_t">Google One-Tap Login & Алиасы</div>
            <div class="t-desc" data-i18n="rm_05_d">
              Вход без паролей в один клик. Сквозная синхронизация истории просмотров, избранного и персональных закладок на десктопе и смартфоне.
            </div>
          </div>
        </div>

        <!-- 06: In-Player Shazam (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-plan">06</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#252632; color:#e4e4e7;" data-i18n="st_plan">Запланировано</span>
              <span class="t-stage">Player Innovation</span>
            </div>
            <div class="t-title" data-i18n="rm_06_t">In-Player Shazam (Музыка в кадре)</div>
            <div class="t-desc" data-i18n="rm_06_d">
              Распознавание саундтрека в реальном времени прямо во время просмотра сцены с возможностью добавить трек в Spotify или Apple Music.
            </div>
          </div>
        </div>

        <!-- 07: Watch Party Sync (Left) -->
        <div class="timeline-row left">
          <div class="timeline-circle node-plan">07</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#252632; color:#e4e4e7;" data-i18n="st_plan">Запланировано</span>
              <span class="t-stage">Social Streaming</span>
            </div>
            <div class="t-title" data-i18n="rm_07_t">Watch Party (Совместный просмотр)</div>
            <div class="t-desc" data-i18n="rm_07_d">
              Синхронный просмотр фильмов друзьями по единой ссылке: синхронная перемотка, реакции и текстово-голосовой чат поверх плеера.
            </div>
          </div>
        </div>

        <!-- 08: AI Movie Assistant (Right) -->
        <div class="timeline-row right">
          <div class="timeline-circle node-plan">08</div>
          <div class="timeline-connector"></div>
          <div class="sketch-card t-card">
            <div class="t-card-head">
              <span class="t-badge" style="background:#252632; color:#e4e4e7;" data-i18n="st_plan">Запланировано</span>
              <span class="t-stage">Frontier AI</span>
            </div>
            <div class="t-title" data-i18n="rm_08_t">AI Кино-Ассистент & Семантический поиск</div>
            <div class="t-desc" data-i18n="rm_08_d">
              Умный подбор кино на естественном языке: «найди напряженный детектив в дождливом городе с неожиданным финалом».
            </div>
          </div>
        </div>
      </div>

      <!-- Final Goal Milestone Card -->
      <div class="timeline-grand">
        <div class="sketch-card grand-card">
          <span class="t-badge" style="background:#fafafa; color:#09090c; font-weight:700;" data-i18n="rm_star_badge">★ Ключевая цель экосистемы</span>
          <div class="t-title" style="font-size:16px; margin:8px 0 6px;" data-i18n="rm_star_t">Shorts & Reels Витрина лучших сцен</div>
          <div class="t-desc" data-i18n="rm_star_d">
            Вертикальная вирусная лента ключевых моментов кино с мгновенным переходом к просмотру полного фильма в один тап без регистрации.
          </div>
        </div>
      </div>
    </section>

    <!-- Section 7: Deal Options -->
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
        hero_status: "Статус: Production (2 месяца в проде) · 0 сторонней рекламы",
        hero_title: "Браузерный кинотеатр без рекламного спама: 100% Share of Voice для одного прямого спонсора",
        hero_sub: "Мы не продаем спам-клики на пиратских сайтах с 15 поп-апами, которые срезает AdBlock. LightStream отдает весь видеоинвентарь одной гемблинг или беттинг сетке на условиях монополии, нативного обхода блокировщиков и 40+ минут внимания на каждого зрителя.",
        hero_hand_note: "42.5 мин средний просмотр (в 18 раз дольше соцсетей)",
        hero_cta_tg: "Забронировать эксклюзив в TG ↗",
        hero_cta_demo: "Открыть кинотеатр lightstream.ws ↗",
        hero_cta_scroll: "Метрики 90д ↓",
        spec_app: "Платформа",
        spec_stack: "Техстек",
        spec_noise: "Рекламный шум",
        spec_noise_val: "0 сторонних баннеров",
        spec_deal: "Формат",
        spec_deal_val: "100% Эксклюзив / M&A",
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
        punch_title: "Тепловая карта активности (Punchcard Heatmap)",
        punch_sub: "Пик внимания: среда 14:00+ и вечерние сеансы 19:00–23:00",
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
        st_done: "В проде ✓",
        st_wip: "В работе ⚡",
        st_plan: "Запланировано",
        rm_01_t: "HLS/DASH Адаптивный видеодвижок",
        rm_01_d: "Мульти-CDN агрегация с автопереключением источников, 1080p, мгновенная буферизация и uBlock-обход за счет нативного рендеринга.",
        rm_02_t: "SEO Оптимизация & Agentic TMDB-синк",
        rm_02_d: "Автоматическая генерация тайтл-карточек, актерских страниц, трейлеров и рейтингов. Быстрая индексация поисковиками и чистая органика.",
        rm_03_t: "Threads & Telegram вирусный трафик",
        rm_03_d: "Автоматизированная фабрика синефильских нарезок и трейлеров. Партизанский маркетинг, привлекающий зрителей с CAC = $0.",
        rm_04_t: "Хаб азиатского контента («Дорамы»)",
        rm_04_d: "Выделенные рельсы и подборки корейских и китайских сериалов с высочайшим retention, глубиной досмотра и повторными визитами.",
        rm_05_t: "Google One-Tap Login & Алиасы",
        rm_05_d: "Вход без паролей в один клик. Сквозная синхронизация истории просмотров, избранного и персональных закладок на десктопе и смартфоне.",
        rm_06_t: "In-Player Shazam (Музыка в кадре)",
        rm_06_d: "Распознавание саундтрека в реальном времени прямо во время просмотра сцены с возможностью добавить трек в Spotify или Apple Music.",
        rm_07_t: "Watch Party (Совместный просмотр)",
        rm_07_d: "Синхронный просмотр фильмов друзьями по единой ссылке: синхронная перемотка, реакции и текстово-голосовой чат поверх плеера.",
        rm_08_t: "AI Кино-Ассистент & Семантический поиск",
        rm_08_d: "Умный подбор кино на естественном языке: «найди напряженный детектив в дождливом городе с неожиданным финалом».",
        rm_star_badge: "★ Ключевая цель экосистемы",
        rm_star_t: "Shorts & Reels Витрина лучших сцен",
        rm_star_d: "Вертикальная вирусная лента ключевых моментов кино с мгновенным переходом к просмотру полного фильма в один тап без регистрации.",
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
        hero_status: "Status: Production (Month 2 Live) · Zero Third-Party Ads",
        hero_title: "Next-Gen Web Cinema: 100% Share of Voice for a Single Direct Advertiser",
        hero_sub: "Zero spam pop-ups killed by AdBlock. Zero competing banners. LightStream gives 100% of our streaming video inventory to one exclusive betting/igaming partner with native ad-block bypass and 40+ minutes of focused attention per viewer.",
        hero_hand_note: "42.5 min avg watch time (18x longer than social media)",
        hero_cta_tg: "Book Exclusive via TG ↗",
        hero_cta_demo: "Open Cinema lightstream.ws ↗",
        hero_cta_scroll: "90-Day Metrics ↓",
        spec_app: "Platform",
        spec_stack: "Tech Stack",
        spec_noise: "Ad Clutter",
        spec_noise_val: "0 Third-Party Banners",
        spec_deal: "Deal Model",
        spec_deal_val: "100% Monopoly / M&A",
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
        punch_title: "Traffic Punchcard Heatmap",
        punch_sub: "Prime-time peaks: Wednesday 14:00+ and evenings 19:00–23:00",
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
        st_done: "Live In Prod ✓",
        st_wip: "In Progress ⚡",
        st_plan: "Planned",
        rm_01_t: "HLS/DASH Adaptive Video Engine",
        rm_01_d: "Multi-CDN aggregation with instant failover, 1080p, ultra-fast buffering, and native uBlock bypass.",
        rm_02_t: "SEO Optimization & Agentic TMDB Sync",
        rm_02_d: "Automated generation of title cards, cast profiles, trailers, and ratings. Rapid indexing and organic search traffic.",
        rm_03_t: "Threads & Telegram Viral Traffic Machine",
        rm_03_d: "Automated distribution pipeline turning cinephile scene clips and trailers into organic traffic at CAC = $0.",
        rm_04_t: "Asian Dramas Hub («Дорамы»)",
        rm_04_d: "Dedicated rails for Korean and Chinese dramas offering massive female viewer retention and frequent repeat visits.",
        rm_05_t: "Google One-Tap Login & Cloud Aliases",
        rm_05_d: "Frictionless password-free onboarding. Full sync of watch history, bookmarks, and likes across desktop and mobile.",
        rm_06_t: "In-Player Shazam (Audio Recognition)",
        rm_06_d: "Instant in-scene song detection with direct links to Spotify and Apple Music right from the player.",
        rm_07_t: "Social Watch Party (Friend Rooms)",
        rm_07_d: "Synchronized movie watching via single invite link: unified playback, voice chat, and live reactions.",
        rm_08_t: "AI Movie Assistant & Semantic Search",
        rm_08_d: "Natural-language movie discovery: «find a tense detective thriller in a rainy city with an unexpected twist».",
        rm_star_badge: "★ Ecosystem North Star",
        rm_star_t: "Vertical Shorts & Reels Scene Showcase",
        rm_star_d: "Viral highlight feed with one-tap transition to watching the full movie with zero friction.",
        deal_title: "Deal Options & Cooperation Models",
        deal_desc: "Three transparent partnership paths — from exclusive monthly sponsorship to full asset acquisition.",
        cta_title: "Discuss Partnership or Request Analytics Access",
        cta_desc: "We are available for a Google Meet call or direct Telegram conversation to negotiate exclusive sponsorship, CPA parameters, or M&A audits.",
        cta_btn_tg: "Contact Founder: @shitmane ↗",
        cta_btn_app: "Open Cinema: lightstream.ws ↗"
      }
    };

    const matrixData = [
      {
        ru: { feature: "Закладки и история (Bookmarks)", note: "Синхронизация прогресса с точностью до секунды" },
        en: { feature: "Bookmarks & Watch History", note: "Second-accurate cross-device progress sync" },
        lightstream: "YES", netflix: "YES", kinopoisk: "YES", pirate_sites: "PARTIAL"
      },
      {
        ru: { feature: "Watch Party (Совместный просмотр)", note: "Синхронное воспроизведение и чат для друзей" },
        en: { feature: "Social Watch Party Rooms", note: "Synchronized playback & chat room for friends" },
        lightstream: "SOON", netflix: "NO", kinopoisk: "NO", pirate_sites: "NO"
      },
      {
        ru: { feature: "Двуязычные субтитры (Smart Subs)", note: "Оригинальный звук + умное переключение дорожек" },
        en: { feature: "Dual Smart Subtitles (RU+EN)", note: "Original audio + instant track switching" },
        lightstream: "YES", netflix: "YES", kinopoisk: "PARTIAL", pirate_sites: "NO"
      },
      {
        ru: { feature: "Горячие клавиши плеера (Hotkeys)", note: "Управление воспроизведением без лишних кликов" },
        en: { feature: "Pro Keyboard Shortcuts", note: "Intuitive hotkey playback controls without menus" },
        lightstream: "YES", netflix: "PARTIAL", kinopoisk: "PARTIAL", pirate_sites: "NO"
      },
      {
        ru: { feature: "Нативная TMDB интеграция", note: "Рейтинги, актеры, трейлеры, даты выхода в 1 клик" },
        en: { feature: "Native TMDB Metadata Integration", note: "Ratings, cast, trailers, and release dates in 1 tap" },
        lightstream: "YES", netflix: "NO", kinopoisk: "NO", pirate_sites: "PARTIAL"
      },
      {
        ru: { feature: "Распознавание музыки (Shazam)", note: "Определение саундтрека прямо во время сцены" },
        en: { feature: "In-Player Shazam Soundtrack Finder", note: "Live scene soundtrack recognition to Spotify" },
        lightstream: "SOON", netflix: "NO", kinopoisk: "NO", pirate_sites: "NO"
      },
      {
        ru: { feature: "Voice EQ (Улучшение голоса)", note: "Выравнивание громкости и усиление диалогов" },
        en: { feature: "Smart Audio & Voice Clarifier", note: "Dialog normalization over explosive sound effects" },
        lightstream: "SOON", netflix: "NO", kinopoisk: "NO", pirate_sites: "NO"
      },
      {
        ru: { feature: "AI Подбор кино по настроению", note: "Поиск кино на естественном языке без шаблонных тегов" },
        en: { feature: "Semantic AI Movie Assistant", note: "Natural language discovery by mood & plot vibes" },
        lightstream: "SOON", netflix: "NO", kinopoisk: "NO", pirate_sites: "NO"
      }
    ];

    const dealsData = [
      {
        badge_ru: "Рекомендуемый", badge_en: "Recommended",
        title_ru: "Генеральное спонсорство (100% Эксклюзив)",
        title_en: "Exclusive General Sponsorship (100% SoV)",
        sub_ru: "Фиксированный месячный ретейнер за весь рекламный инвентарь платформы",
        sub_en: "Fixed monthly retainer securing 100% video inventory across the platform",
        pts_ru: [
          "Полный монопольный эксклюзив без единого конкурента",
          "Интерактивный нативный видео-оверлей перед стартом и на паузе",
          "100% обход AdBlock (нативный рендеринг в канвасе плеера)",
          "Сквозная кликабельная брендированная плашка с переходом",
          "Фиксация ставки на 3–6 месяцев до кратного масштабирования"
        ],
        pts_en: [
          "100% exclusive monopoly without a single competing brand",
          "Interactive native video overlay at start and on pause",
          "100% AdBlock bypass (native WebGL canvas overlay)",
          "Sticky clickable branded player banner",
          "Rate locked for 3–6 months ahead of traffic scaling"
        ],
        for_ru: "Букмекеры и топ-казино, выстраивающие монопольный бренд-оффер",
        for_en: "Top betting & igaming operators building an exclusive brand monopoly"
      },
      {
        badge_ru: "Конверсионный", badge_en: "Performance",
        title_ru: "Эксклюзивный CPA / Hybrid с гарантией объема",
        title_en: "Exclusive CPA / Hybrid with Volume Baseline",
        sub_ru: "Высокая ставка за первый депозит (FTD) + бейслайн под кинозрителя",
        sub_en: "High CPA rate per first-time deposit (FTD) with calibrated player baseline",
        pts_ru: [
          "Персональный промокод и трекер под кинотеатр",
          "Кастомные триггерные кнопки («Смотри без рекламы с бонусом от партнера»)",
          "Раздельный таргетинг по гео (раздельные офферы под РФ, КЗ, Бурж)",
          "Еженедельная сверка и прозрачные когорты конверсий"
        ],
        pts_en: [
          "Dedicated tracking domain and promo codes",
          "Custom CTA triggers («Watch uninterrupted with partner bonus»)",
          "Granular GEO routing (split offers for CIS, US, EU)",
          "Weekly reconciliation and transparent cohort analytics"
        ],
        for_ru: "Партнерские сети с сильным конвертом и гибкими бейслайнами",
        for_en: "Affiliate networks with strong conversion funnels and flexible baselines"
      },
      {
        badge_ru: "M&A / Asset Sale", badge_en: "M&A / Buyout",
        title_ru: "Полный выкуп платформы (Asset / Acqui-hire)",
        title_en: "Full Asset Buyout & Technology Transfer",
        sub_ru: "Передача исходного кода, видеоинфраструктуры, домена и пайплайнов",
        sub_en: "Full handover of source code, video CDN pipelines, domain, and scrapers",
        pts_ru: [
          "Полный стек: SvelteKit + Bun + Hono + HLS/DASH видео-пайплайн",
          "Домен lightstream.ws + сетка сопутствующих каналов дистрибуции",
          "Команда готова сопровождать интеграцию и масштабирование под ключ"
        ],
        pts_en: [
          "Full tech stack: SvelteKit + Bun + Hono + HLS/DASH video pipeline",
          "Primary domain lightstream.ws + satellite viral distribution channels",
          "Engineering team available for turnkey handover and integration"
        ],
        for_ru: "Медиахолдинги и гемблинг-операторы, строящие свою медиасеть",
        for_en: "Media conglomerates & gaming groups launching proprietary media networks"
      }
    ];

    let currentLang = 'ru';

    function init() {
      // Check URL param ?lang=en or localStorage
      const urlParams = new URLSearchParams(window.location.search);
      const paramLang = urlParams.get('lang');
      if (paramLang && (paramLang === 'en' || paramLang === 'ru')) {
        currentLang = paramLang;
      } else {
        const saved = localStorage.getItem('ls_pitch_lang');
        if (saved && (saved === 'en' || saved === 'ru')) {
          currentLang = saved;
        }
      }

      bindDrawer();
      bindCalculator();
      setLang(currentLang, false);
      setStage('current');
    }

    function setLang(lang, pushState = true) {
      currentLang = lang;
      localStorage.setItem('ls_pitch_lang', lang);
      document.documentElement.lang = lang;

      // Update URL query without full reload
      if (pushState) {
        const url = new URL(window.location);
        url.searchParams.set('lang', lang);
        window.history.replaceState({}, '', url);
      }

      // Update lang buttons
      const btnRu = document.getElementById('btnLangRu');
      const btnEn = document.getElementById('btnLangEn');
      if (lang === 'ru') {
        btnRu.classList.add('active');
        btnEn.classList.remove('active');
      } else {
        btnEn.classList.add('active');
        btnRu.classList.remove('active');
      }

      // Translate data-i18n elements
      const dict = i18nData[lang];
      document.querySelectorAll('[data-i18n]').forEach(el => {
        const k = el.getAttribute('data-i18n');
        if (dict[k]) {
          el.textContent = dict[k];
        }
      });

      renderMatrix(lang);
      renderDeals(lang);
    }

    function bindDrawer() {
      const toggle = document.getElementById('burgerToggle');
      const closeBtn = document.getElementById('drawerClose');
      const backdrop = document.getElementById('drawerBackdrop');
      const panel = document.getElementById('drawerPanel');
      const links = panel.querySelectorAll('.drawer-link[data-close]');

      function open() {
        toggle.classList.add('active');
        toggle.setAttribute('aria-expanded', 'true');
        backdrop.classList.add('show');
        panel.classList.add('show');
        document.body.style.overflow = 'hidden';
      }

      function close() {
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
        backdrop.classList.remove('show');
        panel.classList.remove('show');
        document.body.style.overflow = '';
      }

      toggle.addEventListener('click', () => {
        if (panel.classList.contains('show')) close();
        else open();
      });

      closeBtn.addEventListener('click', close);
      backdrop.addEventListener('click', close);

      links.forEach(l => l.addEventListener('click', close));

      document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && panel.classList.contains('show')) close();
      });
    }

    function setStage(stageKey) {
      const stages = {
        current: {
          mau: "5,400+",
          session: "42.5 мин",
          views: "18,500+",
          noteMau_ru: "Органическая база киноманов",
          noteMau_en: "Organic cinephile user base",
          noteViews_ru: "100% чистые досмотры в адаптивном плеере",
          noteViews_en: "100% clean plays in custom player"
        },
        q4_projection: {
          mau: "45,000+",
          session: "44.0 мин",
          views: "160,000+",
          noteMau_ru: "Масштабирование SEO и партизанских каналов",
          noteMau_en: "Scale via SEO & viral organic automation",
          noteViews_ru: "Емкость инвентаря на момент контракта",
          noteViews_en: "Inventory capacity upon deal closing"
        },
        scale: {
          mau: "140,000+",
          session: "45.0 мин",
          views: "520,000+",
          noteMau_ru: "Подключение AI-шортсов и мультиязычной сетки",
          noteMau_en: "Turnkey multi-language & viral shorts network",
          noteViews_ru: "Максимальный объем видеоинвентаря",
          noteViews_en: "Peak streaming video inventory"
        }
      };

      const st = stages[stageKey] || stages.current;
      document.querySelectorAll('.stage-tab').forEach(t => {
        if (t.dataset.stage === stageKey) t.classList.add('active');
        else t.classList.remove('active');
      });

      document.getElementById('valMau').textContent = st.mau;
      document.getElementById('valSession').textContent = st.session;
      document.getElementById('valViews').textContent = st.views;
      document.getElementById('noteMau').textContent = currentLang === 'ru' ? st.noteMau_ru : st.noteMau_en;
      document.getElementById('noteViews').textContent = currentLang === 'ru' ? st.noteViews_ru : st.noteViews_en;
    }

    function bindCalculator() {
      const sliderMau = document.getElementById('sliderMau');
      const sliderCtr = document.getElementById('sliderCtr');
      const dispMau = document.getElementById('calcMauDisplay');
      const dispCtr = document.getElementById('calcCtrDisplay');

      function recalculate() {
        const mau = Number(sliderMau.value);
        const ctr = Number(sliderCtr.value);

        dispMau.textContent = mau.toLocaleString();
        dispCtr.textContent = ctr.toFixed(1) + '%';

        const impressions = Math.round(mau * 3.5);
        const clicks = Math.round(impressions * (ctr / 100));
        const ftdMin = Math.round(clicks * 0.06);
        const ftdMax = Math.round(clicks * 0.10);
        const cpaVal = Math.round(ftdMin * 40);

        document.getElementById('resImpressions').textContent = impressions.toLocaleString();
        document.getElementById('resClicks').textContent = clicks.toLocaleString();
        document.getElementById('resFtd').textContent = `${ftdMin.toLocaleString()} – ${ftdMax.toLocaleString()}`;
        document.getElementById('resVal').textContent = `$${cpaVal.toLocaleString()}+`;
      }

      sliderMau.addEventListener('input', recalculate);
      sliderCtr.addEventListener('input', recalculate);
      recalculate();
    }

    function renderMatrix(lang) {
      const tbody = document.getElementById('matrixBody');
      if (!tbody) return;
      tbody.innerHTML = '';

      function tag(v) {
        if (v === 'YES') return '<span class="tag-yes">YES ✓</span>';
        if (v === 'SOON') return '<span class="tag-soon">SOON ⚡</span>';
        if (v === 'PARTIAL') return '<span class="tag-partial">PARTIAL</span>';
        return '<span class="tag-no">NO ✕</span>';
      }

      matrixData.forEach(row => {
        const item = row[lang] || row.ru;
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <strong>${item.feature}</strong>
            <div style="font-size:11px; color:var(--text-dim); margin-top:2px;">${item.note}</div>
          </td>
          <td>${tag(row.lightstream)}</td>
          <td>${tag(row.netflix)}</td>
          <td>${tag(row.kinopoisk)}</td>
          <td>${tag(row.pirate_sites)}</td>
        `;
        tbody.appendChild(tr);
      });
    }

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

    init();
  </script>
</body>
</html>
'''

output_path = r"D:\lightstream\pitch-site\index.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully compiled hand-drawn blueprint pitch deck to {output_path}! File size: {os.path.getsize(output_path)} bytes")

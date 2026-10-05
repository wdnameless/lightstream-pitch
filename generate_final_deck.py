import os
import json

metrics_path = r"D:\lightstream\pitch-site\metrics.json"
with open(metrics_path, "r", encoding="utf-8") as f:
    metrics_data = json.load(f)

json_str = json.dumps(metrics_data, ensure_ascii=False, indent=2)

matrix_rows_html = ""
for row in metrics_data.get("comparison_matrix", {}).get("rows", []):
    def tag(v):
        if v == "YES": return '<span class="status-tag yes">YES ✓</span>'
        if v == "SOON": return '<span class="status-tag soon">SOON ⚡</span>'
        if v == "PARTIAL": return '<span class="status-tag partial">PARTIAL</span>'
        return '<span class="status-tag no">NO ✕</span>'
    
    matrix_rows_html += f"""            <tr>
              <td>
                <strong>{row['feature']}</strong>
                <div style="font-size: 11px; color: var(--text-dim); margin-top: 2px;">{row['note']}</div>
              </td>
              <td>{tag(row['lightstream'])}</td>
              <td>{tag(row['netflix'])}</td>
              <td>{tag(row['kinopoisk'])}</td>
              <td>{tag(row['pirate_sites'])}</td>
            </tr>\n"""

deals_html = ""
for idx, deal in enumerate(metrics_data.get("deal_options", [])):
    badge = deal.get("badge", f"Опция {idx+1}")
    primary_cls = " primary" if idx == 0 else ""
    pts = "".join([f"<li>{pt}</li>" for pt in deal.get("features", [])])
    deals_html += f"""        <div class="deal-card{primary_cls}">
          <div>
            <span class="deal-badge">{badge}</span>
            <h3 class="deal-title">{deal['title']}</h3>
            <p class="deal-sub">{deal['subtitle']}</p>
            <ul class="deal-points">
              {pts}
            </ul>
          </div>
          <div class="deal-footer">
            Кому подходит: <strong>{deal['best_for']}</strong>
          </div>
        </div>\n"""

html_template = f'''<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <title>LightStream — Инвестиционно-коммерческий бриф и аналитика</title>
  <meta name="description" content="Официальный бриф онлайн-кинотеатра LightStream: верифицированная веб-аналитика, сравнение с Netflix, интерактивный калькулятор ROI, timeline-роадмап фичей.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #09090b;
      --card-bg: #111114;
      --card-border: #222226;
      --card-hover: #18181d;
      --text-main: #fafafa;
      --text-muted: #a1a1aa;
      --text-dim: #71717a;
      --accent-white: #ffffff;
      --accent-green: #10b981;
      --accent-blue: #3b82f6;
      --accent-cyan: #06b6d4;
      --accent-amber: #f59e0b;
      --line: #1c1c20;
      --badge-bg: #18181b;
      --mono: 'JetBrains Mono', monospace;
      --sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }}

    html, body {{
      width: 100%;
      max-width: 100vw;
      overflow-x: hidden;
      background-color: var(--bg);
      color: var(--text-main);
      font-family: var(--sans);
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
    }}

    body {{
      padding-bottom: 96px;
    }}

    .container {{
      width: 100%;
      max-width: 1120px;
      margin: 0 auto;
      padding: 0 20px;
      box-sizing: border-box;
    }}

    /* Sticky Header */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(9, 9, 11, 0.95);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--line);
      padding: 12px 0;
      width: 100%;
    }}

    .nav {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: relative;
    }}

    .logo-group {{
      display: flex;
      align-items: center;
      gap: 10px;
      text-decoration: none;
      color: inherit;
      min-height: 40px;
      flex-shrink: 0;
    }}

    .logo-icon {{
      width: 24px;
      height: 24px;
      background: var(--text-main);
      border-radius: 5px;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      flex-shrink: 0;
    }}

    .logo-icon::before {{
      content: '';
      width: 0;
      height: 0;
      border-top: 5px solid transparent;
      border-bottom: 5px solid transparent;
      border-left: 8px solid #09090b;
      margin-left: 2px;
    }}

    .logo-text {{
      font-size: 16px;
      font-weight: 700;
      letter-spacing: -0.02em;
    }}

    .header-badge {{
      font-family: var(--mono);
      font-size: 11px;
      padding: 3px 8px;
      border-radius: 4px;
      background: var(--badge-bg);
      border: 1px solid var(--card-border);
      color: var(--text-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      white-space: nowrap;
    }}

    .header-right {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-shrink: 0;
    }}

    .btn {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 500;
      text-decoration: none;
      transition: all 0.15s ease;
      cursor: pointer;
      white-space: nowrap;
      min-height: 38px;
    }}

    .btn-secondary {{
      background: #18181b;
      border: 1px solid var(--card-border);
      color: var(--text-main);
    }}

    .btn-secondary:hover {{
      background: var(--card-hover);
      border-color: #3f3f46;
    }}

    .btn-primary {{
      background: var(--text-main);
      color: #09090b;
      font-weight: 600;
      border: 1px solid var(--text-main);
    }}

    .btn-primary:hover {{
      background: #e4e4e7;
    }}

    /* Dropdown Menu Trigger & Popover */
    .menu-btn {{
      display: inline-flex;
      align-items: center;
      gap: 7px;
      padding: 8px 14px;
      border-radius: 6px;
      background: #141418;
      border: 1px solid var(--card-border);
      color: var(--text-main);
      font-size: 13px;
      font-family: var(--mono);
      cursor: pointer;
      transition: all 0.15s ease;
      min-height: 38px;
      flex-shrink: 0;
    }}

    .menu-btn:hover, .menu-btn.active {{
      background: #202026;
      border-color: #52525b;
    }}

    .menu-btn .chevron {{
      font-size: 10px;
      transition: transform 0.2s ease;
    }}

    .menu-btn.active .chevron {{
      transform: rotate(180deg);
    }}

    .dropdown-menu {{
      position: absolute;
      top: calc(100% + 10px);
      right: 0;
      width: 320px;
      max-width: calc(100vw - 32px);
      background-color: #111116;
      border: 1px solid #2e2e34;
      border-radius: 10px;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.95);
      padding: 12px;
      display: none;
      flex-direction: column;
      gap: 6px;
      z-index: 1000;
      animation: dropdownFadeIn 0.18s ease forwards;
    }}

    @keyframes dropdownFadeIn {{
      from {{ opacity: 0; transform: translateY(-8px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .dropdown-menu.show {{
      display: flex;
    }}

    .dropdown-category {{
      font-size: 10px;
      font-family: var(--mono);
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 8px 10px 4px;
    }}

    .dropdown-link {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 12px;
      border-radius: 6px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 13px;
      transition: all 0.12s ease;
    }}

    .dropdown-link:hover {{
      background: #1c1c22;
      color: var(--text-main);
    }}

    .dropdown-link span {{
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .dropdown-link .tag {{
      font-family: var(--mono);
      font-size: 10px;
      color: var(--text-dim);
    }}

    .dropdown-divider {{
      height: 1px;
      background: var(--line);
      margin: 4px 0;
    }}

    .dropdown-actions-mobile {{
      display: none;
      flex-direction: column;
      gap: 8px;
      padding-top: 6px;
    }}

    /* Hero Section */
    .hero {{
      padding: 52px 0 40px;
      border-bottom: 1px solid var(--line);
    }}

    .hero-eyebrow {{
      font-family: var(--mono);
      font-size: 12px;
      color: var(--text-dim);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .pulse-dot {{
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--accent-green);
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.8);
      flex-shrink: 0;
    }}

    h1 {{
      font-size: clamp(24px, 4vw, 42px);
      font-weight: 700;
      line-height: 1.25;
      letter-spacing: -0.03em;
      margin-bottom: 18px;
      max-width: 960px;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}

    .hero-sub {{
      font-size: clamp(14px, 2vw, 17px);
      color: var(--text-muted);
      line-height: 1.6;
      max-width: 860px;
      margin-bottom: 28px;
      word-wrap: break-word;
      overflow-wrap: break-word;
    }}

    .hero-sub strong {{
      color: var(--text-main);
    }}

    .hero-meta-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 12px;
      font-family: var(--mono);
      font-size: 12px;
      padding: 16px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
    }}

    .hero-meta-item {{
      display: flex;
      flex-direction: column;
      gap: 3px;
    }}

    .hero-meta-item .label {{
      color: var(--text-dim);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .hero-meta-item .val {{
      color: var(--text-main);
      font-weight: 500;
      word-break: break-all;
    }}

    /* Section Global */
    .section {{
      padding: 60px 0;
      border-bottom: 1px solid var(--line);
    }}

    .section-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-end;
      margin-bottom: 30px;
      flex-wrap: wrap;
      gap: 16px;
    }}

    .section-title {{
      font-size: clamp(20px, 3vw, 26px);
      font-weight: 600;
      letter-spacing: -0.02em;
      margin-bottom: 6px;
      word-wrap: break-word;
    }}

    .section-desc {{
      font-size: 14px;
      color: var(--text-muted);
      max-width: 720px;
      line-height: 1.55;
      word-wrap: break-word;
    }}

    /* Infographic Card Containers */
    .info-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 24px;
      position: relative;
      overflow: hidden;
      max-width: 100%;
    }}

    .info-card-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 20px;
      flex-wrap: wrap;
      gap: 10px;
    }}

    .info-card-title {{
      font-size: 16px;
      font-weight: 600;
      letter-spacing: -0.01em;
      word-wrap: break-word;
    }}

    .info-card-sub {{
      font-size: 12px;
      color: var(--text-dim);
      margin-top: 2px;
      word-wrap: break-word;
    }}

    /* Infographics Grid (Dual Top) */
    .infographics-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}

    /* SVG Traffic Chart */
    .traffic-chart-wrap {{
      width: 100%;
      height: 220px;
      position: relative;
      overflow: hidden;
    }}

    .traffic-chart-svg {{
      width: 100%;
      height: 100%;
      display: block;
    }}

    .chart-stats-row {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 10px;
      margin-top: 18px;
      padding-top: 16px;
      border-top: 1px solid var(--line);
    }}

    .chart-stat-item {{
      display: flex;
      flex-direction: column;
    }}

    .chart-stat-item .k {{
      font-size: 11px;
      font-family: var(--mono);
      color: var(--text-dim);
      text-transform: uppercase;
    }}

    .chart-stat-item .v {{
      font-size: 18px;
      font-weight: 700;
      font-family: var(--mono);
      color: var(--text-main);
      margin-top: 2px;
    }}

    .chart-stat-item .tag {{
      font-size: 11px;
      color: var(--accent-green);
      font-family: var(--mono);
    }}

    /* Radar Chart (Netflix vs LightStream) */
    .radar-chart-wrap {{
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: 16px;
      width: 100%;
    }}

    .radar-svg-box {{
      width: 100%;
      max-width: 360px;
      height: 250px;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .radar-legend {{
      display: flex;
      justify-content: center;
      gap: 16px;
      font-family: var(--mono);
      font-size: 12px;
      flex-wrap: wrap;
    }}

    .legend-item {{
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .legend-color {{
      width: 10px;
      height: 10px;
      border-radius: 2px;
      flex-shrink: 0;
    }}

    .color-lightstream {{
      background: #fafafa;
      box-shadow: 0 0 6px rgba(255, 255, 255, 0.6);
    }}

    .color-netflix {{
      background: #ef4444;
    }}

    /* Devices & GEO Breakdown */
    .devices-geo-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
      margin-bottom: 24px;
    }}

    .bar-list {{
      display: flex;
      flex-direction: column;
      gap: 14px;
    }}

    .bar-item {{
      display: flex;
      flex-direction: column;
      gap: 5px;
    }}

    .bar-item-header {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      gap: 8px;
    }}

    .bar-item-title {{
      font-weight: 500;
      display: flex;
      align-items: center;
      gap: 8px;
      word-wrap: break-word;
    }}

    .bar-item-val {{
      font-family: var(--mono);
      color: var(--text-main);
      font-weight: 600;
      white-space: nowrap;
    }}

    .bar-track {{
      height: 6px;
      background: #1c1c22;
      border-radius: 3px;
      overflow: hidden;
      width: 100%;
    }}

    .bar-fill {{
      height: 100%;
      background: var(--text-main);
      border-radius: 3px;
      transition: width 0.4s ease;
    }}

    /* Punchcard Heatmap */
    .punchcard-card {{
      margin-bottom: 24px;
      max-width: 100%;
      overflow: hidden;
    }}

    .punchcard-scroll {{
      width: 100%;
      max-width: 100%;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      display: block;
      padding-bottom: 8px;
    }}

    .punchcard-table {{
      min-width: 580px;
      width: 100%;
      border-collapse: collapse;
      font-size: 11px;
      font-family: var(--mono);
    }}

    .punchcard-table th {{
      padding: 6px 8px;
      color: var(--text-dim);
      font-weight: 500;
      text-align: center;
    }}

    .punchcard-table td {{
      padding: 8px;
      text-align: center;
    }}

    .punchcard-day-col {{
      text-align: left !important;
      color: var(--text-muted);
      font-weight: 600;
      width: 50px;
    }}

    .punch-dot {{
      display: inline-block;
      border-radius: 50%;
      background: var(--text-main);
      transition: all 0.15s ease;
    }}

    .punch-dot:hover {{
      transform: scale(1.4);
      box-shadow: 0 0 10px rgba(255, 255, 255, 0.8);
    }}

    /* Stage Controller & Metrics */
    .stage-switch {{
      display: inline-flex;
      background: #121215;
      padding: 4px;
      border-radius: 8px;
      border: 1px solid var(--card-border);
      gap: 4px;
      max-width: 100%;
    }}

    .stage-tab {{
      padding: 6px 14px;
      font-size: 12px;
      font-family: var(--mono);
      border-radius: 6px;
      background: transparent;
      border: none;
      color: var(--text-dim);
      cursor: pointer;
      transition: all 0.15s ease;
      white-space: nowrap;
    }}

    .stage-tab.active {{
      background: #27272a;
      color: var(--text-main);
      font-weight: 500;
    }}

    .metrics-grid {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-bottom: 20px;
    }}

    .metric-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 20px;
      transition: border-color 0.15s ease;
      max-width: 100%;
    }}

    .metric-card:hover {{
      border-color: #3f3f46;
    }}

    .metric-label {{
      font-size: 11px;
      color: var(--text-dim);
      font-family: var(--mono);
      margin-bottom: 10px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .metric-value {{
      font-size: clamp(24px, 3.2vw, 32px);
      font-weight: 700;
      font-family: var(--mono);
      color: var(--text-main);
      letter-spacing: -0.03em;
      margin-bottom: 4px;
    }}

    .metric-note {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.4;
      word-wrap: break-word;
    }}

    .growth-insight-box {{
      background: #121216;
      border: 1px solid #27272a;
      border-left: 3px solid #fafafa;
      border-radius: 6px;
      padding: 16px 20px;
      font-size: 13px;
      color: var(--text-muted);
      line-height: 1.6;
      word-wrap: break-word;
    }}

    .growth-insight-box strong {{
      color: var(--text-main);
    }}

    /* Interactive Sponsor ROI Calculator */
    .calculator-box {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 24px;
      margin-top: 24px;
      max-width: 100%;
    }}

    .calc-controls {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 24px;
      margin-bottom: 24px;
    }}

    .calc-field label {{
      display: flex;
      justify-content: space-between;
      font-size: 12px;
      font-family: var(--mono);
      color: var(--text-dim);
      margin-bottom: 10px;
      gap: 8px;
    }}

    .calc-field label span strong {{
      color: var(--text-main);
      font-size: 14px;
    }}

    .calc-slider {{
      width: 100%;
      height: 8px;
      background: #27272a;
      border-radius: 4px;
      outline: none;
      -webkit-appearance: none;
      cursor: pointer;
    }}

    .calc-slider::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      background: #fafafa;
      border: 2px solid #09090b;
      box-shadow: 0 0 6px rgba(255, 255, 255, 0.4);
    }}

    .calc-results {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 14px;
      background: #09090b;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
    }}

    .calc-res-item {{
      display: flex;
      flex-direction: column;
    }}

    .calc-res-label {{
      font-size: 11px;
      font-family: var(--mono);
      color: var(--text-dim);
      margin-bottom: 4px;
    }}

    .calc-res-val {{
      font-size: clamp(18px, 2.5vw, 22px);
      font-weight: 700;
      font-family: var(--mono);
      color: var(--text-main);
    }}

    .calc-res-sub {{
      font-size: 11px;
      color: var(--text-muted);
    }}

    /* Comparison Matrix */
    .matrix-wrap {{
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      margin-bottom: 20px;
      width: 100%;
      max-width: 100%;
      display: block;
    }}

    .matrix-table {{
      width: 100%;
      min-width: 680px;
      border-collapse: collapse;
      font-size: 13px;
      text-align: left;
    }}

    .matrix-table th, .matrix-table td {{
      padding: 14px 18px;
      border-bottom: 1px solid var(--line);
    }}

    .matrix-table th {{
      background: #141418;
      font-family: var(--mono);
      font-size: 11px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--text-dim);
    }}

    .matrix-table tr:last-child td {{
      border-bottom: none;
    }}

    .status-tag {{
      display: inline-flex;
      align-items: center;
      padding: 2px 7px;
      border-radius: 4px;
      font-family: var(--mono);
      font-size: 11px;
      font-weight: 600;
      white-space: nowrap;
    }}

    .status-tag.yes {{
      background: #064e3b;
      color: #34d399;
    }}

    .status-tag.soon {{
      background: #27272a;
      color: #e4e4e7;
      border: 1px solid #3f3f46;
    }}

    .status-tag.partial {{
      background: #422006;
      color: #fbbf24;
    }}

    .status-tag.no {{
      background: #1c1917;
      color: #78716c;
    }}

    .score-summary-banner {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 16px 20px;
      background: #141419;
      border: 1px solid var(--card-border);
      border-radius: 8px;
      flex-wrap: wrap;
      gap: 12px;
      max-width: 100%;
    }}

    .score-banner-text {{
      font-size: 13px;
      color: var(--text-muted);
      max-width: 720px;
      flex: 1 1 300px;
    }}

    .score-banner-score {{
      font-family: var(--mono);
      font-size: 17px;
      font-weight: 700;
      color: var(--text-main);
      white-space: nowrap;
    }}

    /* ==========================================================================
       FEATURE TIMELINE ARROW (Based on Reference: Vertical central arrow with alternating branch nodes)
       ========================================================================== */
    .timeline-container {{
      position: relative;
      max-width: 980px;
      margin: 40px auto 20px;
      padding: 20px 0 60px;
      width: 100%;
    }}

    /* Central vertical line / arrow stem */
    .timeline-stem {{
      position: absolute;
      top: 0;
      bottom: 20px;
      left: 50%;
      width: 4px;
      background: linear-gradient(180deg, #3f3f46 0%, #71717a 50%, #ffffff 100%);
      transform: translateX(-50%);
      border-radius: 2px;
    }}

    /* Downward arrow tip at bottom of stem */
    .timeline-stem::after {{
      content: '';
      position: absolute;
      bottom: -16px;
      left: 50%;
      transform: translateX(-50%);
      width: 0;
      height: 0;
      border-left: 10px solid transparent;
      border-right: 10px solid transparent;
      border-top: 18px solid #ffffff;
      filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.7));
    }}

    .timeline-item {{
      position: relative;
      margin-bottom: 36px;
      width: 50%;
      display: flex;
      align-items: center;
      box-sizing: border-box;
    }}

    .timeline-item.left {{
      left: 0;
      padding-right: 54px;
      justify-content: flex-end;
    }}

    .timeline-item.right {{
      left: 50%;
      padding-left: 54px;
      justify-content: flex-start;
    }}

    /* Central circle marker on the stem */
    .timeline-node {{
      position: absolute;
      top: 50%;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      background: #111115;
      border: 3px solid #71717a;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 700;
      font-family: var(--mono);
      color: #fafafa;
      transform: translateY(-50%);
      z-index: 5;
      box-shadow: 0 0 0 4px #09090b;
      transition: all 0.2s ease;
      flex-shrink: 0;
    }}

    .timeline-item.left .timeline-node {{
      right: -17px;
    }}

    .timeline-item.right .timeline-node {{
      left: -17px;
    }}

    /* Connecting horizontal dashed arm */
    .timeline-arm {{
      position: absolute;
      top: 50%;
      height: 2px;
      border-top: 2px dashed #52525b;
      width: 38px;
      z-index: 1;
    }}

    .timeline-item.left .timeline-arm {{
      right: 17px;
    }}

    .timeline-item.right .timeline-arm {{
      left: 17px;
    }}

    /* Status variants for nodes */
    .node-live {{
      border-color: #10b981;
      background: #064e3b;
      box-shadow: 0 0 10px rgba(16, 185, 129, 0.5), 0 0 0 4px #09090b;
    }}

    .node-progress {{
      border-color: #3b82f6;
      background: #1e3a8a;
      box-shadow: 0 0 10px rgba(59, 130, 246, 0.5), 0 0 0 4px #09090b;
    }}

    .node-planned {{
      border-color: #e4e4e7;
      background: #27272a;
      box-shadow: 0 0 8px rgba(228, 228, 231, 0.3), 0 0 0 4px #09090b;
    }}

    /* Content Card */
    .timeline-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 8px;
      padding: 16px 20px;
      width: 100%;
      max-width: 410px;
      position: relative;
      transition: all 0.2s ease;
      box-sizing: border-box;
    }}

    .timeline-card:hover {{
      border-color: #52525b;
      transform: translateY(-2px);
    }}

    .timeline-header-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .timeline-badge {{
      font-size: 10px;
      font-family: var(--mono);
      padding: 2px 6px;
      border-radius: 4px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
    }}

    .timeline-stage-tag {{
      font-size: 10px;
      font-family: var(--mono);
      color: var(--text-dim);
    }}

    .timeline-title {{
      font-size: 14px;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 4px;
      line-height: 1.35;
      word-wrap: break-word;
    }}

    .timeline-desc {{
      font-size: 12px;
      color: var(--text-muted);
      line-height: 1.5;
      word-wrap: break-word;
    }}

    /* Final Grand Milestone Card */
    .timeline-final-item {{
      max-width: 580px;
      margin: 40px auto 0;
      text-align: center;
      position: relative;
      z-index: 10;
      box-sizing: border-box;
    }}

    .timeline-final-card {{
      background: #141419;
      border: 1px solid #52525b;
      border-radius: 10px;
      padding: 22px;
      box-shadow: 0 0 30px rgba(255, 255, 255, 0.05);
      box-sizing: border-box;
    }}

    /* Deals Section */
    .deals-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 16px;
    }}

    .deal-card {{
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 10px;
      padding: 24px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-sizing: border-box;
      max-width: 100%;
    }}

    .deal-card.primary {{
      border-color: #52525b;
      box-shadow: 0 0 20px rgba(255, 255, 255, 0.04);
    }}

    .deal-badge {{
      font-family: var(--mono);
      font-size: 10px;
      padding: 2px 6px;
      background: #27272a;
      border-radius: 4px;
      margin-bottom: 12px;
      display: inline-block;
      color: var(--text-muted);
      align-self: flex-start;
    }}

    .deal-title {{
      font-size: 17px;
      font-weight: 600;
      margin-bottom: 6px;
      letter-spacing: -0.01em;
      word-wrap: break-word;
    }}

    .deal-sub {{
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 18px;
      line-height: 1.45;
      word-wrap: break-word;
    }}

    .deal-points {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 12px;
      color: var(--text-muted);
      margin-bottom: 24px;
      flex-grow: 1;
    }}

    .deal-points li {{
      padding-left: 14px;
      position: relative;
      word-wrap: break-word;
    }}

    .deal-points li::before {{
      content: '•';
      position: absolute;
      left: 0;
      color: var(--text-dim);
    }}

    .deal-footer {{
      font-size: 11px;
      color: var(--text-dim);
      border-top: 1px solid var(--line);
      padding-top: 12px;
      word-wrap: break-word;
    }}

    /* CTA Section */
    .cta-box {{
      background: #141418;
      border: 1px solid #3f3f46;
      border-radius: 12px;
      padding: 36px 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 20px;
      margin-top: 48px;
      box-sizing: border-box;
      max-width: 100%;
    }}

    .cta-content {{
      max-width: 640px;
      flex: 1 1 300px;
    }}

    .cta-title {{
      font-size: clamp(20px, 3vw, 24px);
      font-weight: 700;
      margin-bottom: 8px;
      letter-spacing: -0.02em;
      word-wrap: break-word;
    }}

    .cta-desc {{
      font-size: 14px;
      color: var(--text-muted);
      line-height: 1.55;
      word-wrap: break-word;
    }}

    .cta-actions {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex-shrink: 0;
    }}

    /* Footer */
    footer {{
      margin-top: 56px;
      font-size: 12px;
      color: var(--text-dim);
      font-family: var(--mono);
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 12px;
      padding-top: 24px;
      border-top: 1px solid var(--line);
      width: 100%;
    }}

    /* Responsive Breakpoints & Mobile Adaptations */
    @media (max-width: 992px) {{
      .infographics-grid, .devices-geo-grid {{
        grid-template-columns: 1fr;
      }}
      .deals-grid {{
        grid-template-columns: 1fr;
      }}
      .hero-meta-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .metrics-grid {{
        grid-template-columns: repeat(2, 1fr);
      }}
      .calc-controls {{
        grid-template-columns: 1fr;
      }}
      .calc-results {{
        grid-template-columns: repeat(2, 1fr);
      }}
    }}

    /* Mobile Timeline Adaptation (Arrow aligned to the left, cards stack cleanly) */
    @media (max-width: 768px) {{
      .timeline-container {{
        padding: 10px 0 40px;
        margin: 20px auto;
      }}
      .timeline-stem {{
        left: 20px;
        transform: none;
      }}
      .timeline-item {{
        width: 100%;
        left: 0 !important;
        padding-left: 54px !important;
        padding-right: 0 !important;
        justify-content: flex-start !important;
        box-sizing: border-box;
      }}
      .timeline-node {{
        left: 3px !important;
        right: auto !important;
      }}
      .timeline-arm {{
        left: 20px !important;
        right: auto !important;
        width: 34px;
      }}
      .timeline-card {{
        max-width: 100%;
        padding: 14px 16px;
        box-sizing: border-box;
      }}
      .timeline-final-item {{
        padding-left: 54px;
        text-align: left;
        margin-top: 24px;
        box-sizing: border-box;
      }}
    }}

    @media (max-width: 640px) {{
      .container {{
        padding: 0 16px;
      }}
      .logo-group .header-badge {{
        display: none;
      }}
      .nav {{
        gap: 8px;
      }}
      .header-right .btn {{
        display: none;
      }}
      .dropdown-actions-mobile {{
        display: flex;
      }}
      .dropdown-menu {{
        position: fixed;
        top: 60px;
        left: 14px;
        right: 14px;
        width: auto;
        max-width: none;
        background-color: #101014;
        border: 1px solid #3f3f46;
        border-radius: 12px;
        box-shadow: 0 20px 50px rgba(0, 0, 0, 0.95);
        max-height: 82vh;
        overflow-y: auto;
      }}
      .hero {{
        padding: 36px 0 32px;
      }}
      .section {{
        padding: 44px 0;
      }}
      .hero-meta-grid {{
        grid-template-columns: 1fr;
        gap: 10px;
      }}
      .metrics-grid {{
        grid-template-columns: 1fr;
      }}
      .calc-results {{
        grid-template-columns: 1fr;
      }}
      .chart-stats-row {{
        grid-template-columns: repeat(2, 1fr);
        gap: 12px;
      }}
      .stage-switch {{
        width: 100%;
        overflow-x: auto;
      }}
      .stage-tab {{
        flex: 1;
        text-align: center;
        padding: 8px 10px;
      }}
      .score-summary-banner {{
        flex-direction: column;
        align-items: flex-start;
        gap: 10px;
      }}
      .score-banner-score {{
        font-size: 15px;
      }}
      .cta-box {{
        padding: 24px 20px;
      }}
      .cta-actions {{
        width: 100%;
      }}
      .cta-actions .btn {{
        width: 100%;
      }}
      footer {{
        flex-direction: column;
        align-items: flex-start;
      }}
    }}
  </style>
</head>
<body>

  <!-- Sticky Header with Dropdown Navigation -->
  <header>
    <div class="container nav">
      <a href="https://app.lightstream.ws" target="_blank" class="logo-group">
        <div class="logo-icon"></div>
        <div class="logo-text">LightStream</div>
        <span class="header-badge">M&A & Deal Brief</span>
      </a>

      <div class="header-right">
        <a href="https://app.lightstream.ws" target="_blank" class="btn btn-secondary">Платформа ↗</a>
        <a href="https://t.me/shitmane" target="_blank" class="btn btn-primary">Связаться в TG</a>

        <!-- Dropdown Menu Trigger Button -->
        <button class="menu-btn" id="menuToggle" aria-expanded="false" aria-label="Открыть навигационное меню">
          <span>Разделы</span>
          <span class="chevron">▼</span>
        </button>

        <!-- Dropdown Popover Menu -->
        <div class="dropdown-menu" id="dropdownMenu">
          <div class="dropdown-category">Аналитика & Метрики</div>
          <a href="#analytics" class="dropdown-link" data-close>
            <span>📈 Трафик & Динамика 90 дней</span>
            <span class="tag">Live</span>
          </a>
          <a href="#radar" class="dropdown-link" data-close>
            <span>🎯 Радар: LightStream vs Netflix</span>
            <span class="tag">7/9</span>
          </a>
          <a href="#devices-geo" class="dropdown-link" data-close>
            <span>🌍 Устройства & ГЕО Сплит</span>
            <span class="tag">5 стран</span>
          </a>
          <a href="#punchcard" class="dropdown-link" data-close>
            <span>⏱ Карта активности (Heatmap)</span>
            <span class="tag">Пики</span>
          </a>
          <a href="#metrics" class="dropdown-link" data-close>
            <span>📊 Проекции MAU & Досмотры</span>
            <span class="tag">Q4 / Q1</span>
          </a>

          <div class="dropdown-divider"></div>
          <div class="dropdown-category">Инструменты & Продукт</div>
          <a href="#calculator" class="dropdown-link" data-close>
            <span>🧮 Калькулятор отдачи (ROI)</span>
            <span class="tag">FTD</span>
          </a>
          <a href="#matrix" class="dropdown-link" data-close>
            <span>📋 Матрица фич и технологий</span>
            <span class="tag">Matrix</span>
          </a>
          <a href="#roadmap" class="dropdown-link" data-close>
            <span>🏹 Timeline-роадмап фичей</span>
            <span class="tag">Arrow</span>
          </a>
          <a href="#deals" class="dropdown-link" data-close>
            <span>💼 Форматы сотрудничества</span>
            <span class="tag">Офферы</span>
          </a>

          <div class="dropdown-actions-mobile">
            <div class="dropdown-divider"></div>
            <a href="https://app.lightstream.ws" target="_blank" class="btn btn-secondary" style="width:100%;">Открыть платформу ↗</a>
            <a href="https://t.me/shitmane" target="_blank" class="btn btn-primary" style="width:100%;">Написать фаундеру: @shitmane</a>
          </div>
        </div>
      </div>
    </div>
  </header>

  <main class="container">

    <!-- Hero Section -->
    <section class="hero">
      <div class="hero-eyebrow">
        <span class="pulse-dot"></span>
        <span>Статус: Production (2 месяца в проде) · 0 сторонней рекламы</span>
      </div>
      <h1>Браузерный кинотеатр нового поколения: 100% Share of Voice для одного прямого рекламодателя</h1>
      <p class="hero-sub">
        Мы не продаем спам-клики на пиратских сайтах с 15 поп-апами, которые блокирует AdBlock. 
        LightStream отдает весь видеоинвентарь <strong>одному генеральному партнеру</strong> на условиях монопольного присутствия, нативного обхода блокировщиков и 40+ минут непрерывного внимания на каждого зрителя.
      </p>

      <div class="hero-meta-grid">
        <div class="hero-meta-item">
          <span class="label">Платформа</span>
          <span class="val">app.lightstream.ws</span>
        </div>
        <div class="hero-meta-item">
          <span class="label">Техстек</span>
          <span class="val">SvelteKit · Bun · Hono · HLS</span>
        </div>
        <div class="hero-meta-item">
          <span class="label">Рекламный шум</span>
          <span class="val">0 сторонних баннеров</span>
        </div>
        <div class="hero-meta-item">
          <span class="label">Форматы сделки</span>
          <span class="val">Спонсорство / CPA / M&A</span>
        </div>
      </div>
    </section>

    <!-- Section 1: Infographics — Traffic Dynamics & Radar Matrix -->
    <section class="section" id="analytics">
      <div class="section-header">
        <div>
          <h2 class="section-title">Верифицированная аналитика и продуктовые метрики</h2>
          <p class="section-desc">
            Визуализация реальных данных продакшн-дашборда за последние 90 дней: динамика роста трафика, радар функционала и технологические преимущества.
          </p>
        </div>
      </div>

      <div class="infographics-grid">
        <!-- Infographic 1: Traffic Dynamics Chart -->
        <div class="info-card">
          <div class="info-card-header">
            <div>
              <div class="info-card-title">Динамика просмотров за 90 дней (7 июл – 3 окт)</div>
              <div class="info-card-sub">Взрывной органический рост в сентябре с пиком >2,100 просмотров/сутки</div>
            </div>
            <span class="header-badge" style="color:var(--accent-green); border-color:#064e3b;">+100% Growth</span>
          </div>

          <div class="traffic-chart-wrap">
            <svg class="traffic-chart-svg" viewBox="0 0 500 200" preserveAspectRatio="none">
              <defs>
                <linearGradient id="barGrad" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0%" stop-color="#ffffff" stop-opacity="0.9"/>
                  <stop offset="100%" stop-color="#71717a" stop-opacity="0.4"/>
                </linearGradient>
              </defs>
              <!-- Grid lines -->
              <line x1="0" y1="40" x2="500" y2="40" stroke="#1c1c22" stroke-dasharray="4 4"/>
              <line x1="0" y1="90" x2="500" y2="90" stroke="#1c1c22" stroke-dasharray="4 4"/>
              <line x1="0" y1="140" x2="500" y2="140" stroke="#1c1c22" stroke-dasharray="4 4"/>
              <line x1="0" y1="180" x2="500" y2="180" stroke="#27272a"/>

              <!-- Bars -->
              <rect x="35" y="170" width="40" height="10" rx="3" fill="#2e2e36"/>
              <rect x="125" y="145" width="40" height="35" rx="3" fill="#3f3f46"/>
              <rect x="215" y="115" width="40" height="65" rx="3" fill="#52525b"/>
              <rect x="305" y="25" width="45" height="155" rx="4" fill="url(#barGrad)"/>
              <rect x="395" y="80" width="40" height="100" rx="3" fill="#71717a"/>

              <!-- Peak indicator badge -->
              <circle cx="327" cy="25" r="4" fill="#fafafa"/>
              <line x1="327" y1="25" x2="327" y2="10" stroke="#fafafa" stroke-width="1.5"/>
              <text x="327" y="6" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Пик 2.1k/день</text>

              <!-- Month labels -->
              <text x="55" y="196" fill="#71717a" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Июль</text>
              <text x="145" y="196" fill="#71717a" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Авг (1-15)</text>
              <text x="235" y="196" fill="#71717a" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Авг (16-31)</text>
              <text x="327" y="196" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Сент (Пик)</text>
              <text x="415" y="196" fill="#71717a" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="middle">Сент (Ядро)</text>
            </svg>
          </div>

          <div class="chart-stats-row">
            <div class="chart-stat-item">
              <span class="k">Просмотры</span>
              <span class="v">26.6k</span>
              <span class="tag">↑ 100%</span>
            </div>
            <div class="chart-stat-item">
              <span class="k">Сессии</span>
              <span class="v">5.82k</span>
              <span class="tag">↑ 100%</span>
            </div>
            <div class="chart-stat-item">
              <span class="k">Уники</span>
              <span class="v">2.88k</span>
              <span class="tag">Органика</span>
            </div>
            <div class="chart-stat-item">
              <span class="k">Глубина</span>
              <span class="v">4m 18s</span>
              <span class="tag">0% спама</span>
            </div>
          </div>
        </div>

        <!-- Infographic 2: Radar Chart (Netflix vs LightStream) -->
        <div class="info-card" id="radar">
          <div class="info-card-header">
            <div>
              <div class="info-card-title">Радар функционала: LightStream vs Netflix</div>
              <div class="info-card-sub">6 осей сравнения: плеер, библиотека, умные субтитры, ИИ и интеграции</div>
            </div>
            <span class="header-badge" style="color:#fafafa; border-color:#52525b;">Счет 7/9</span>
          </div>

          <div class="radar-chart-wrap">
            <div class="radar-svg-box">
              <svg viewBox="0 0 380 280" width="100%" height="100%">
                <!-- Outer ring (R=95) -->
                <polygon points="190,40 272,88 272,182 190,230 108,182 108,88" fill="none" stroke="#222228" stroke-width="1.5"/>
                <!-- Mid ring (R=63) -->
                <polygon points="190,72 245,103 245,167 190,198 135,167 135,103" fill="none" stroke="#1c1c22" stroke-width="1"/>
                <!-- Inner ring (R=32) -->
                <polygon points="190,103 218,119 218,151 190,167 162,151 162,119" fill="none" stroke="#18181d" stroke-width="1"/>

                <!-- Axes -->
                <line x1="190" y1="135" x2="190" y2="40" stroke="#222228" stroke-width="1"/>
                <line x1="190" y1="135" x2="272" y2="88" stroke="#222228" stroke-width="1"/>
                <line x1="190" y1="135" x2="272" y2="182" stroke="#222228" stroke-width="1"/>
                <line x1="190" y1="135" x2="190" y2="230" stroke="#222228" stroke-width="1"/>
                <line x1="190" y1="135" x2="108" y2="182" stroke="#222228" stroke-width="1"/>
                <line x1="190" y1="135" x2="108" y2="88" stroke="#222228" stroke-width="1"/>

                <!-- Netflix Polygon -->
                <polygon points="190,55 246,101 210,146 190,154 128,168 128,99" 
                         fill="rgba(239, 68, 68, 0.12)" stroke="#ef4444" stroke-width="1.8" stroke-dasharray="4 3"/>

                <!-- LightStream Polygon -->
                <polygon points="190,44 268,91 264,178 190,218 112,179 112,91" 
                         fill="rgba(250, 250, 250, 0.22)" stroke="#fafafa" stroke-width="2.2"/>
                <circle cx="190" cy="44" r="3.5" fill="#fafafa"/>
                <circle cx="268" cy="91" r="3.5" fill="#fafafa"/>
                <circle cx="264" cy="178" r="3.5" fill="#fafafa"/>
                <circle cx="190" cy="218" r="3.5" fill="#fafafa"/>
                <circle cx="112" cy="179" r="3.5" fill="#fafafa"/>
                <circle cx="112" cy="91" r="3.5" fill="#fafafa"/>

                <!-- Labels -->
                <text x="190" y="24" fill="#fafafa" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Библиотека (TMDB)</text>
                <text x="282" y="89" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="start">Плеер (UX)</text>
                <text x="280" y="186" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="start">Интеграции</text>
                <text x="190" y="254" fill="#fafafa" font-size="10.5" font-family="'JetBrains Mono', monospace" text-anchor="middle" font-weight="600">Аудио / Voice</text>
                <text x="98" y="186" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">Субтитры (RU+EN)</text>
                <text x="98" y="89" fill="#fafafa" font-size="10" font-family="'JetBrains Mono', monospace" text-anchor="end">ИИ-поиск</text>
              </svg>
            </div>

            <div class="radar-legend">
              <div class="legend-item">
                <span class="legend-color color-lightstream"></span>
                <span><strong>LightStream</strong> (7/9 фич, 100% SoV)</span>
              </div>
              <div class="legend-item">
                <span class="legend-color color-netflix"></span>
                <span style="color:#ef4444;">Netflix (2/9 фич)</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Infographics Strip 2: Devices & Geo Breakdown -->
      <div class="devices-geo-grid" id="devices-geo">
        <!-- Devices & Browsers -->
        <div class="info-card">
          <div class="info-card-header">
            <div>
              <div class="info-card-title">Браузеры и окружение пользователей</div>
              <div class="info-card-sub">Преобладание десктопного и премиального iOS-трафика</div>
            </div>
            <span class="header-badge">Environment</span>
          </div>

          <div class="bar-list">
            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">💻 Google Chrome (Desktop / Win / Mac)</span>
                <span class="bar-item-val">43% <span style="font-size:11px; color:var(--text-dim);">(1,210)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 43%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">📱 iOS Safari (iPhone / iPad)</span>
                <span class="bar-item-val">19% <span style="font-size:11px; color:var(--text-dim);">(538)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 19%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">📱 iOS Webview (Telegram / In-App)</span>
                <span class="bar-item-val">14% <span style="font-size:11px; color:var(--text-dim);">(391)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 14%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🌐 Chrome Webview & Другие</span>
                <span class="bar-item-val">9% <span style="font-size:11px; color:var(--text-dim);">(254)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 9%;"></div>
              </div>
            </div>
          </div>
        </div>

        <!-- Geographic Split -->
        <div class="info-card">
          <div class="info-card-header">
            <div>
              <div class="info-card-title">Верифицированная география аудитории</div>
              <div class="info-card-sub">Четкое разделение по странам, платежным шлюзам и среднему чеку</div>
            </div>
            <span class="header-badge">Top Locations</span>
          </div>

          <div class="bar-list">
            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🇺🇸 США (United States) <span class="header-badge" style="padding:1px 5px; font-size:9px;">Tier-1 Global</span></span>
                <span class="bar-item-val">24% <span style="font-size:11px; color:var(--text-dim);">(499)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 24%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🇧🇾 Беларусь (Belarus) <span class="header-badge" style="padding:1px 5px; font-size:9px;">Tier-1 CIS</span></span>
                <span class="bar-item-val">14% <span style="font-size:11px; color:var(--text-dim);">(294)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 14%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🇺🇦 Украина (Ukraine) <span class="header-badge" style="padding:1px 5px; font-size:9px;">Tier-1 CIS</span></span>
                <span class="bar-item-val">14% <span style="font-size:11px; color:var(--text-dim);">(291)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 14%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🇰🇿 Казахстан (Kazakhstan) <span class="header-badge" style="padding:1px 5px; font-size:9px;">Tier-2 CIS</span></span>
                <span class="bar-item-val">12% <span style="font-size:11px; color:var(--text-dim);">(247)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 12%;"></div>
              </div>
            </div>

            <div class="bar-item">
              <div class="bar-item-header">
                <span class="bar-item-title">🇵🇱 Польша & ЕС (Poland) <span class="header-badge" style="padding:1px 5px; font-size:9px;">Tier-1 EU</span></span>
                <span class="bar-item-val">11% <span style="font-size:11px; color:var(--text-dim);">(222)</span></span>
              </div>
              <div class="bar-track">
                <div class="bar-fill" style="width: 11%;"></div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Infographic Component 4: Punchcard Heatmap -->
      <div class="info-card punchcard-card" id="punchcard">
        <div class="info-card-header">
          <div>
            <div class="info-card-title">Тепловая карта активности (Traffic Punchcard Heatmap)</div>
            <div class="info-card-sub">Плотность визитов по дням недели и часам суток. Пик внимания: среда 14:00+ и вечерние сеансы 19:00–23:00</div>
          </div>
          <span class="header-badge" style="color:var(--accent-green); border-color:#064e3b;">Prime-Time</span>
        </div>

        <div class="punchcard-scroll">
          <table class="punchcard-table">
            <thead>
              <tr>
                <th class="punchcard-day-col">День</th>
                <th>00ч</th>
                <th>03ч</th>
                <th>06ч</th>
                <th>09ч</th>
                <th>12ч</th>
                <th>14ч ★</th>
                <th>16ч</th>
                <th>18ч</th>
                <th>20ч</th>
                <th>22ч</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="punchcard-day-col">Вс</td>
                <td><span class="punch-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="punch-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:4px; height:4px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="punch-dot" style="width:10px; height:10px; opacity:0.7;"></span></td>
                <td><span class="punch-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
              </tr>
              <tr>
                <td class="punchcard-day-col">Пн</td>
                <td><span class="punch-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="punch-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="punch-dot" style="width:10px; height:10px; opacity:0.7;"></span></td>
                <td><span class="punch-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="punch-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
              </tr>
              <tr>
                <td class="punchcard-day-col">Вт</td>
                <td><span class="punch-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="punch-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="punch-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
              <tr style="background: rgba(255,255,255,0.03);">
                <td class="punchcard-day-col" style="color:#fafafa;">Ср ★</td>
                <td><span class="punch-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="punch-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="punch-dot" style="width:3px; height:3px; opacity:0.25;"></span></td>
                <td><span class="punch-dot" style="width:7px; height:7px; opacity:0.5;"></span></td>
                <td><span class="punch-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="punch-dot" style="width:18px; height:18px; opacity:1.0; box-shadow:0 0 12px rgba(255,255,255,0.8);"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:17px; height:17px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
              </tr>
              <tr>
                <td class="punchcard-day-col">Чт</td>
                <td><span class="punch-dot" style="width:6px; height:6px; opacity:0.5;"></span></td>
                <td><span class="punch-dot" style="width:3px; height:3px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="punch-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
              <tr>
                <td class="punchcard-day-col">Пт</td>
                <td><span class="punch-dot" style="width:7px; height:7px; opacity:0.55;"></span></td>
                <td><span class="punch-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:5px; height:5px; opacity:0.4;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
                <td><span class="punch-dot" style="width:13px; height:13px; opacity:0.85;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:17px; height:17px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
              </tr>
              <tr>
                <td class="punchcard-day-col">Сб</td>
                <td><span class="punch-dot" style="width:8px; height:8px; opacity:0.6;"></span></td>
                <td><span class="punch-dot" style="width:4px; height:4px; opacity:0.35;"></span></td>
                <td><span class="punch-dot" style="width:2px; height:2px; opacity:0.2;"></span></td>
                <td><span class="punch-dot" style="width:4px; height:4px; opacity:0.3;"></span></td>
                <td><span class="punch-dot" style="width:9px; height:9px; opacity:0.65;"></span></td>
                <td><span class="punch-dot" style="width:11px; height:11px; opacity:0.75;"></span></td>
                <td><span class="punch-dot" style="width:12px; height:12px; opacity:0.8;"></span></td>
                <td><span class="punch-dot" style="width:15px; height:15px; opacity:0.95;"></span></td>
                <td><span class="punch-dot" style="width:16px; height:16px; opacity:1.0;"></span></td>
                <td><span class="punch-dot" style="width:14px; height:14px; opacity:0.9;"></span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

    <!-- Section 2: Audience Metrics & Dynamic Projections -->
    <section class="section" id="metrics">
      <div class="section-header">
        <div>
          <h2 class="section-title">Аудитория и динамические проекции роста</h2>
          <p class="section-desc">
            Кинотрафик оценивается через MAU (месячный охват) и досмотры. Переключайте стадию для оценки текущего факта и планового масштаба на момент подписания контракта.
          </p>
        </div>
        <div class="stage-switch" id="stageControls">
          <button class="stage-tab active" data-stage="current">Факт (Месяц 2)</button>
          <button class="stage-tab" data-stage="q4_projection">Run-Rate (Q4)</button>
          <button class="stage-tab" data-stage="scale">Масштаб (Q1)</button>
        </div>
      </div>

      <div class="metrics-grid">
        <div class="metric-card">
          <div class="metric-label">MAU (Месячный охват)</div>
          <div class="metric-value" id="valMau">5,400+</div>
          <div class="metric-note" id="noteMau">Органическая база киноманов</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Средняя кино-сессия</div>
          <div class="metric-value" id="valSession">42.5 мин</div>
          <div class="metric-note">В 18 раз дольше соцсетей и прелендингов</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Просмотры видео / мес</div>
          <div class="metric-value" id="valViews">18,500+</div>
          <div class="metric-note" id="noteViews">100% чистые досмотры в адаптивном плеере</div>
        </div>
        <div class="metric-card">
          <div class="metric-label">Share of Voice</div>
          <div class="metric-value">100%</div>
          <div class="metric-note">Ноль сторонних брендов, ноль конкурентных слотов</div>
        </div>
      </div>

      <div class="growth-insight-box">
        <strong>💡 Заметка для медиабайинга и инвестиционного комитета:</strong>
        Согласование корпоративных интеграций с топ-букмекерами (1xBet, Winline, Fonbet, Parimatch) занимает от 1.5 до 3 месяцев. 
        За время прохождения комплаенса и интеграции LightStream масштабируется в соответствии с run-rate показателями (вкладка <em>Run-Rate Q4</em>). 
        Ранний вход позволяет зафиксировать ставку генерального спонсора до кратного роста стоимости инвентаря.
      </div>

      <!-- Interactive Sponsor ROI Calculator -->
      <div class="calculator-box" id="calculator">
        <div class="info-card-header">
          <div>
            <div class="info-card-title">Калькулятор отдачи от спонсорства (Sponsor ROI Estimator)</div>
            <div class="info-card-sub">Рассчитайте потенциальный объем показов и депозитов при эксклюзивном брендинге плеера</div>
          </div>
          <span class="header-badge">Interactive Tool</span>
        </div>

        <div class="calc-controls">
          <div class="calc-field">
            <label>
              <span>Месячный охват аудитории (MAU)</span>
              <span><strong id="calcMauDisplay">45,000</strong> зрителей</span>
            </label>
            <input type="range" min="5000" max="150000" step="5000" value="45000" class="calc-slider" id="sliderMau">
          </div>
          <div class="calc-field">
            <label>
              <span>Конверсия в переход из плеера (CTR)</span>
              <span><strong id="calcCtrDisplay">3.5%</strong> (нативный оверлей)</span>
            </label>
            <input type="range" min="1.0" max="7.0" step="0.5" value="3.5" class="calc-slider" id="sliderCtr">
          </div>
        </div>

        <div class="calc-results">
          <div class="calc-res-item">
            <div class="calc-res-label">Видео-показы / мес</div>
            <div class="calc-res-val" id="resImpressions">160,000</div>
            <div class="calc-res-sub">100% Share of Voice</div>
          </div>
          <div class="calc-res-item">
            <div class="calc-res-label">Прямые клики на оффер</div>
            <div class="calc-res-val" id="resClicks">5,600</div>
            <div class="calc-res-sub">Без потери на AdBlock</div>
          </div>
          <div class="calc-res-item">
            <div class="calc-res-label">Прогноз FTD (Депозитов)</div>
            <div class="calc-res-val" id="resFtd">336 – 560</div>
            <div class="calc-res-sub">При CR 6–10% рег2деп</div>
          </div>
          <div class="calc-res-item">
            <div class="calc-res-label">Ценность трафика (CPA экв.)</div>
            <div class="calc-res-val" id="resVal">$16,800+</div>
            <div class="calc-res-sub">При ставке $40 FTD</div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: Feature Matrix -->
    <section class="section" id="matrix">
      <div class="section-header">
        <div>
          <h2 class="section-title">Honest comparison. Data instead of marketing.</h2>
          <p class="section-desc">
            Сравнение технологического стека и фич LightStream с Netflix, Кинопоиском и пиратскими сайтами.
          </p>
        </div>
        <span class="header-badge" style="color:var(--accent-green); border-color:#064e3b;">LightStream: 7/9 фич</span>
      </div>

      <div class="matrix-wrap">
        <table class="matrix-table" id="comparisonTable">
          <thead>
            <tr>
              <th style="width: 32%;">Критерий / Фича</th>
              <th style="width: 17%;">LightStream</th>
              <th style="width: 17%;">Netflix</th>
              <th style="width: 17%;">Кинопоиск</th>
              <th style="width: 17%;">Пиратские сайты</th>
            </tr>
          </thead>
          <tbody id="matrixBody">
{matrix_rows_html}          </tbody>
        </table>
      </div>

      <div class="score-summary-banner">
        <div class="score-banner-text">
          LightStream совмещает удобство премиального стриминга с инструментами нового поколения (TMDB-синхронизация, распознавание музыки, умные субтитры), оставляя пиратские сайты в прошлом веке.
        </div>
        <div class="score-banner-score">
          Счет: LightStream 7/9 vs Netflix 2/9
        </div>
      </div>
    </section>

    <!-- =======================================================================
         Section 4: FEATURE TIMELINE ARROW (Roadmap by Features without fixed dates)
         ======================================================================= -->
    <section class="section" id="roadmap">
      <div class="section-header">
        <div>
          <h2 class="section-title">Продуктовый Timeline-роадмап</h2>
          <p class="section-desc">
            Вектор развития продукта: от уже запущенного видеодвижка до социальных и ИИ-инноваций следующего поколения. Без привязки к абстрактным датам — фокус на ценности и фичах.
          </p>
        </div>
        <span class="header-badge">Timeline Arrow</span>
      </div>

      <div class="timeline-container">
        <!-- Central vertical arrow stem -->
        <div class="timeline-stem"></div>

        <!-- Milestone 01 (Left): HLS/DASH Streaming Engine -->
        <div class="timeline-item left">
          <div class="timeline-node node-live">01</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#064e3b; color:#34d399;">В проде ✓</span>
              <span class="timeline-stage-tag">Core Engine</span>
            </div>
            <div class="timeline-title">HLS/DASH Адаптивный видеодвижок</div>
            <div class="timeline-desc">
              Мульти-CDN агрегация с автопереключением источников, 1080p, мгновенная буферизация и uBlock-обход за счет нативного рендеринга.
            </div>
          </div>
        </div>

        <!-- Milestone 02 (Right): SEO + Agentic Pipeline -->
        <div class="timeline-item right">
          <div class="timeline-node node-live">02</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#064e3b; color:#34d399;">В проде ✓</span>
              <span class="timeline-stage-tag">Growth Pipeline</span>
            </div>
            <div class="timeline-title">SEO Оптимизация & Agentic TMDB-синк</div>
            <div class="timeline-desc">
              Автоматическая генерация тайтл-карточек, актерских страниц, трейлеров и рейтингов. Быстрая индексация поисковиками и чистая органика.
            </div>
          </div>
        </div>

        <!-- Milestone 03 (Left): Threads & Telegram Automation -->
        <div class="timeline-item left">
          <div class="timeline-node node-progress">03</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#1e3a8a; color:#60a5fa;">В работе ⚡</span>
              <span class="timeline-stage-tag">Viral Distribution</span>
            </div>
            <div class="timeline-title">Threads & Telegram вирусный трафик</div>
            <div class="timeline-desc">
              Автоматизированная фабрика синефильских нарезок и трейлеров. Партизанский маркетинг, привлекающий десятки тысяч зрителей с CAC = $0.
            </div>
          </div>
        </div>

        <!-- Milestone 04 (Right): Asian Dramas / Дорамы Hub -->
        <div class="timeline-item right">
          <div class="timeline-node node-progress">04</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#1e3a8a; color:#60a5fa;">В работе ⚡</span>
              <span class="timeline-stage-tag">Content Expansion</span>
            </div>
            <div class="timeline-title">Хаб азиатского контента («Дорамы»)</div>
            <div class="timeline-desc">
              Выделенные рельсы и подборки корейских и китайских сериалов с высочайшим retention, глубиной досмотра и повторными визитами.
            </div>
          </div>
        </div>

        <!-- Milestone 05 (Left): Google One-Tap & Aliases -->
        <div class="timeline-item left">
          <div class="timeline-node node-progress">05</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#1e3a8a; color:#60a5fa;">В работе ⚡</span>
              <span class="timeline-stage-tag">User Identity</span>
            </div>
            <div class="timeline-title">Google One-Tap Login & Алиасы</div>
            <div class="timeline-desc">
              Вход без паролей в один клик. Сквозная синхронизация истории просмотров, избранного и персональных закладок на десктопе и смартфоне.
            </div>
          </div>
        </div>

        <!-- Milestone 06 (Right): In-Player Shazam -->
        <div class="timeline-item right">
          <div class="timeline-node node-planned">06</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#27272a; color:#e4e4e7;">Запланировано</span>
              <span class="timeline-stage-tag">Player Innovation</span>
            </div>
            <div class="timeline-title">In-Player Shazam (Музыка в кадре)</div>
            <div class="timeline-desc">
              Распознавание саундтрека в реальном времени прямо во время просмотра сцены с возможностью добавить трек в Spotify или Apple Music.
            </div>
          </div>
        </div>

        <!-- Milestone 07 (Left): Watch Party Sync -->
        <div class="timeline-item left">
          <div class="timeline-node node-planned">07</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#27272a; color:#e4e4e7;">Запланировано</span>
              <span class="timeline-stage-tag">Social Streaming</span>
            </div>
            <div class="timeline-title">Watch Party (Совместный просмотр)</div>
            <div class="timeline-desc">
              Синхронный просмотр фильмов друзьями по единой ссылке: единая перемотка, реакции и текстово-голосовой чат поверх плеера.
            </div>
          </div>
        </div>

        <!-- Milestone 08 (Right): AI Movie Assistant -->
        <div class="timeline-item right">
          <div class="timeline-node node-planned">08</div>
          <div class="timeline-arm"></div>
          <div class="timeline-card">
            <div class="timeline-header-row">
              <span class="timeline-badge" style="background:#27272a; color:#e4e4e7;">Запланировано</span>
              <span class="timeline-stage-tag">Frontier AI</span>
            </div>
            <div class="timeline-title">AI Кино-Ассистент & Семантический поиск</div>
            <div class="timeline-desc">
              Умный подбор кино на естественном языке: «найди напряженный детектив в дождливом городе с неожиданным финалом».
            </div>
          </div>
        </div>
      </div>

      <!-- Final Arrow Milestone Card -->
      <div class="timeline-final-item">
        <div class="timeline-final-card">
          <span class="timeline-badge" style="background:#fafafa; color:#09090b; font-weight:700;">★ Ключевая цель экосистемы</span>
          <div class="timeline-title" style="font-size:16px; margin:8px 0 6px;">Shorts & Reels Витрина лучших сцен</div>
          <div class="timeline-desc">
            Вертикальная вирусная лента ключевых моментов кино с мгновенным переходом к просмотру полного фильма в один тап без регистрации.
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: Deal Formats -->
    <section class="section" id="deals">
      <div class="section-header">
        <div>
          <h2 class="section-title">Форматы сотрудничества</h2>
          <p class="section-desc">
            Мы открыты к трем прозрачным моделям — от фиксированного рекламного ретейнера до полной продажи актива с передачей кода и инфраструктуры.
          </p>
        </div>
      </div>

      <div class="deals-grid" id="dealsContainer">
{deals_html}      </div>
    </section>

    <!-- Direct CTA -->
    <div class="cta-box">
      <div class="cta-content">
        <div class="cta-title">Обсудить партнерство или запросить доступ к метрикам</div>
        <div class="cta-desc">
          Мы открыты к созвону в Google Meet или диалогу в Telegram для обсуждения фиксированной ставки спонсорства, параметров CPA-бейслайна или M&A аудита платформы.
        </div>
      </div>
      <div class="cta-actions">
        <a href="https://t.me/shitmane" target="_blank" class="btn btn-primary" style="padding: 12px 24px; font-size: 14px;">
          Написать фаундеру: @shitmane ↗
        </a>
        <a href="mailto:good22067@gmail.com" class="btn btn-secondary" style="padding: 10px 20px;">
          good22067@gmail.com
        </a>
      </div>
    </div>

    <!-- Footer -->
    <footer>
      <div>LightStream Media Group · app.lightstream.ws</div>
      <div id="updatedAtLabel">Обновлено: 2026-10-05</div>
    </footer>

  </main>

  <script>
    const DEFAULT_METRICS = {json_str};
    let appData = DEFAULT_METRICS;

    async function init() {{
      bindDropdownMenu();
      bindCalculator();

      try {{
        const res = await fetch('./metrics.json?v=' + Date.now());
        if (res.ok) {{
          appData = await res.json();
          document.getElementById('updatedAtLabel').textContent = 'Обновлено: ' + (appData.updated_at || '2026-10-05');
        }}
      }} catch (err) {{
        console.warn('Using embedded fallback metrics:', err);
      }}

      renderMatrix();
      renderDeals();
      bindStageSwitch();
      updateStage('current');
    }}

    function bindDropdownMenu() {{
      const toggle = document.getElementById('menuToggle');
      const menu = document.getElementById('dropdownMenu');
      const links = document.querySelectorAll('.dropdown-link[data-close]');

      function toggleMenu(e) {{
        e.stopPropagation();
        const isOpen = menu.classList.contains('show');
        if (isOpen) {{
          menu.classList.remove('show');
          toggle.classList.remove('active');
          toggle.setAttribute('aria-expanded', 'false');
        }} else {{
          menu.classList.add('show');
          toggle.classList.add('active');
          toggle.setAttribute('aria-expanded', 'true');
        }}
      }}

      function closeMenu() {{
        menu.classList.remove('show');
        toggle.classList.remove('active');
        toggle.setAttribute('aria-expanded', 'false');
      }}

      toggle.addEventListener('click', toggleMenu);

      links.forEach(link => {{
        link.addEventListener('click', closeMenu);
      }});

      document.addEventListener('click', (e) => {{
        if (!menu.contains(e.target) && e.target !== toggle && !toggle.contains(e.target)) {{
          closeMenu();
        }}
      }});

      document.addEventListener('keydown', (e) => {{
        if (e.key === 'Escape') closeMenu();
      }});
    }}

    function updateStage(stageKey) {{
      if (!appData.stages) return;
      const stage = appData.stages[stageKey] || appData.stages.current;
      document.getElementById('valMau').textContent = Number(stage.mau).toLocaleString() + '+';
      document.getElementById('valSession').textContent = stage.avg_session_min + ' мин';
      document.getElementById('valViews').textContent = Number(stage.monthly_views).toLocaleString() + '+';
      document.getElementById('noteMau').textContent = stage.note_mau || 'Органическая база киноманов';
      document.getElementById('noteViews').textContent = stage.note_views || '100% чистые досмотры в адаптивном плеере';
    }}

    function bindStageSwitch() {{
      const tabs = document.querySelectorAll('.stage-tab');
      tabs.forEach(tab => {{
        tab.addEventListener('click', () => {{
          tabs.forEach(t => t.classList.remove('active'));
          tab.classList.add('active');
          updateStage(tab.dataset.stage);
        }});
      }});
    }}

    function bindCalculator() {{
      const sliderMau = document.getElementById('sliderMau');
      const sliderCtr = document.getElementById('sliderCtr');
      const dispMau = document.getElementById('calcMauDisplay');
      const dispCtr = document.getElementById('calcCtrDisplay');

      function recalculate() {{
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
        document.getElementById('resFtd').textContent = `${{ftdMin.toLocaleString()}} – ${{ftdMax.toLocaleString()}}`;
        document.getElementById('resVal').textContent = `$${{cpaVal.toLocaleString()}}+`;
      }}

      sliderMau.addEventListener('input', recalculate);
      sliderCtr.addEventListener('input', recalculate);
      recalculate();
    }}

    function renderMatrix() {{
      const tbody = document.getElementById('matrixBody');
      if (!tbody || !appData.comparison_matrix) return;
      tbody.innerHTML = '';

      function renderStatus(val) {{
        if (val === 'YES') return '<span class="status-tag yes">YES ✓</span>';
        if (val === 'SOON') return '<span class="status-tag soon">SOON ⚡</span>';
        if (val === 'PARTIAL') return '<span class="status-tag partial">PARTIAL</span>';
        return '<span class="status-tag no">NO ✕</span>';
      }}

      appData.comparison_matrix.rows.forEach(row => {{
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>
            <strong>${{row.feature}}</strong>
            <div style="font-size: 11px; color: var(--text-dim); margin-top: 2px;">${{row.note}}</div>
          </td>
          <td>${{renderStatus(row.lightstream)}}</td>
          <td>${{renderStatus(row.netflix)}}</td>
          <td>${{renderStatus(row.kinopoisk)}}</td>
          <td>${{renderStatus(row.pirate_sites)}}</td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function renderDeals() {{
      const container = document.getElementById('dealsContainer');
      if (!container || !appData.deal_options) return;
      container.innerHTML = '';
      appData.deal_options.forEach((deal, idx) => {{
        const card = document.createElement('div');
        card.className = 'deal-card' + (idx === 0 ? ' primary' : '');
        const points = (deal.features || []).map(f => `<li>${{f}}</li>`).join('');
        card.innerHTML = `
          <div>
            <span class="deal-badge">${{deal.badge || 'Опция ' + (idx + 1)}}</span>
            <h3 class="deal-title">${{deal.title}}</h3>
            <p class="deal-sub">${{deal.subtitle}}</p>
            <ul class="deal-points">${{points}}</ul>
          </div>
          <div class="deal-footer">
            Кому подходит: <strong>${{deal.best_for}}</strong>
          </div>
        `;
        container.appendChild(card);
      }});
    }}

    init();
  </script>
</body>
</html>
'''

with open(r"D:\lightstream\pitch-site\index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print(f"Generated index.html with static pre-rendered fallback & mobile responsive rules! Size: {os.path.getsize(r'D:\lightstream\pitch-site\index.html')} bytes")

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.optimize import brentq
import random

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Raising Equity Lab",
    page_icon="📈",
    layout="wide"
)

# =========================================================
# HELPERS
# =========================================================

def pct(x, d=4):
    return f"{round(x, d)}%"

def currency(x):
    return f"₹{x:,.2f}"

# =========================================================
# TITLE
# =========================================================

st.title("📈 Experiential Learning Lab: Raising Equity")

st.markdown("""
Welcome to the **Raising Equity Learning Platform**.

This app covers every method by which a firm raises equity capital:

- Introduction to Equity Financing
- Initial Public Offering (IPO) — Process, Pricing & Valuation
- Follow-on Public Offer (FPO)
- Rights Issue
- Bonus Issue (Stock Dividend)
- Private Placement
- Qualified Institutional Placement (QIP)
- Preferential Allotment
- Employee Stock Option Plan (ESOP)
- American & Global Depository Receipts (ADR/GDR)
- Venture Capital (VC) Funding
- Private Equity (PE)
- Convertible Instruments (CCPS, CCD, Warrants)
- Retained Earnings as Internal Equity
- Cost of New Equity vs Retained Earnings
- Dilution Analysis & EPS Impact
- Regulatory Framework (SEBI, Companies Act)
- Valuation Methods for Equity Issuance
- Green Shoe Option & Price Stabilisation

through:

✅ Interactive calculators  
✅ Real Indian corporate examples  
✅ Step-by-step solvers  
✅ Visual diagrams  
✅ Quiz engine  
✅ Common mistakes  
✅ Formula cheat sheet  
✅ Case-based learning (Zomato IPO)
""")

# =========================================================
# SIDEBAR
# =========================================================

menu = st.sidebar.radio(
    "Choose Module",
    [
        "Introduction",
        # ── PUBLIC EQUITY ─────────────────────────────────
        "Initial Public Offering (IPO)",
        "IPO Pricing & Book Building",
        "IPO Valuation Methods",
        "Follow-on Public Offer (FPO)",
        "Rights Issue",
        "Bonus Issue",
        # ── PRIVATE EQUITY ───────────────────────────────
        "Private Placement",
        "Qualified Institutional Placement (QIP)",
        "Preferential Allotment",
        "Venture Capital (VC)",
        "Private Equity (PE)",
        # ── INSTRUMENTS ──────────────────────────────────
        "ESOP (Employee Stock Options)",
        "Convertible Instruments",
        "ADR & GDR",
        # ── ANALYSIS ─────────────────────────────────────
        "Retained Earnings vs New Equity",
        "Cost of New Equity (Flotation Costs)",
        "Dilution Analysis",
        "EPS & Book Value Impact",
        # ── REGULATORY ───────────────────────────────────
        "SEBI Regulations",
        "Companies Act 2013 — Equity Provisions",
        # ── TOOLS ────────────────────────────────────────
        "Equity Instrument Comparison",
        "Step-by-Step Solver",
        "AI Hint System",
        "Quiz Engine",
        "Excel Formula Trainer",
        "Formula Cheat Sheet",
        "Common Student Mistakes",
        "Advanced Quiz Bank",
        "Progress Tracker",
        "Case-Based Learning (Zomato IPO)",
    ]
)

# =========================================================
# INTRODUCTION
# =========================================================

if menu == "Introduction":

    st.header("📘 Introduction to Raising Equity")

    st.markdown("""
## What is Equity Financing?

Equity financing involves raising capital by **selling ownership stakes** in the company.
Unlike debt, equity:
- Does **not** require repayment
- Carries **no fixed interest obligation**
- Gives shareholders **residual claim** on profits and assets
- Dilutes existing ownership

---

## Why Do Firms Raise Equity?
""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("""
**Growth Funding**
- Fund new projects / capex
- Enter new markets
- Acquire competitors
- R&D investment
        """)

    with col2:
        st.warning("""
**Balance Sheet Strengthening**
- Reduce debt burden
- Improve credit rating
- Lower interest costs
- Prepare for economic downturns
        """)

    with col3:
        st.success("""
**Liquidity & Exit**
- Early investors exit (VC/PE)
- Promoter partial monetisation
- Employee wealth creation (ESOPs)
- Market price discovery
        """)

    st.markdown("""
---

## Methods of Raising Equity — Overview
""")

    methods_df = pd.DataFrame({
        "Method": [
            "IPO (Initial Public Offering)",
            "FPO (Follow-on Public Offer)",
            "Rights Issue",
            "Bonus Issue",
            "QIP (Qualified Institutional Placement)",
            "Preferential Allotment",
            "Private Placement",
            "ESOP",
            "Venture Capital",
            "Private Equity",
            "ADR / GDR",
            "Convertible Instruments",
        ],
        "Type": [
            "Public","Public","Public","Capitalisation",
            "Private","Private","Private","Internal",
            "Private","Private","International","Hybrid"
        ],
        "Raises Cash?": [
            "✅","✅","✅","❌ (no cash)",
            "✅","✅","✅","Deferred",
            "✅","✅","✅","Deferred"
        ],
        "Dilutes Existing Owners?": [
            "✅","✅","✅ (if not taken)",
            "✅ (EPS dilutes)","✅","✅","✅","✅ (on exercise)",
            "✅","✅","✅","✅ (on conversion)"
        ],
        "Typical Use": [
            "First listing; VC/PE exit",
            "Listed firm needs more capital",
            "Existing shareholders given priority",
            "Reward shareholders; improve liquidity",
            "Fast equity raise from institutions",
            "Strategic allotment to specific investors",
            "Small private firms pre-IPO",
            "Attract and retain talent",
            "Early-stage startups",
            "Growth / buyout of mature firms",
            "Raise capital from foreign markets",
            "Bridge financing; structured deals"
        ]
    })

    st.dataframe(methods_df, use_container_width=True)

    st.info("""
**Indian Context:**
- SEBI regulates all public equity issuances
- Companies Act 2013 governs private equity and allotments
- NSE & BSE are the primary listing exchanges
- India has the world's largest IPO pipeline in recent years (2022-2024)
""")

# =========================================================
# IPO
# =========================================================

elif menu == "Initial Public Offering (IPO)":

    st.header("🏦 Initial Public Offering (IPO)")

    st.markdown("""
## What is an IPO?

An **Initial Public Offering (IPO)** is the first time a privately held company
offers its shares to the general public and gets listed on a stock exchange.

## Two Types of IPO in India

| Type | Description | Example |
|---|---|---|
| **Fresh Issue** | Company issues new shares; funds go to company | LIC IPO (partial fresh) |
| **Offer for Sale (OFS)** | Existing shareholders sell their shares; funds go to sellers | Zomato (mix of both) |
| **Mixed** | Both fresh issue and OFS | Most common |
""")

    st.subheader("📋 IPO Process in India (SEBI Framework)")

    steps_ipo = [
        ("1. Decision & Approval", "Board resolution, EGM approval, appoint investment bankers (Book Running Lead Managers — BRLMs)"),
        ("2. Due Diligence", "Legal, financial, and business due diligence by BRLMs"),
        ("3. Draft Red Herring Prospectus (DRHP)", "Filed with SEBI. Contains company details, financials, risk factors, use of proceeds"),
        ("4. SEBI Review", "SEBI reviews DRHP; issues observations (typically 30 days)"),
        ("5. Red Herring Prospectus (RHP)", "Filed after SEBI approval; price band included"),
        ("6. Roadshow", "Company management meets institutional investors (QIBs) to generate interest"),
        ("7. Book Building / Bidding", "3-day bidding window. Three categories: QIB (50%), NII (15%), RII (35%)"),
        ("8. Price Determination", "Cut-off price set based on demand; typically at band top if oversubscribed"),
        ("9. Allotment & Listing", "Shares allotted within 6 days; listing on NSE/BSE within T+6 days"),
    ]

    for step, desc in steps_ipo:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.markdown(f"**{step}**")
        with col2:
            st.markdown(desc)
        st.divider()

    st.subheader("📊 IPO Subscription Categories (SEBI Rules)")

    categories = pd.DataFrame({
        "Category": ["Qualified Institutional Buyers (QIB)", "Non-Institutional Investors (NII/HNI)", "Retail Individual Investors (RII)"],
        "Allocation": ["50% of issue size", "15% of issue size", "35% of issue size"],
        "Who": ["FIIs, Mutual Funds, Banks, Insurance", "HNI / Corporate (>₹2L application)", "Individuals applying ≤ ₹2 Lakh"],
        "Allotment Method": ["Proportionate", "Proportionate", "Lottery if oversubscribed"],
        "Lock-up": ["No mandatory lock-up", "No lock-up", "No lock-up"],
    })

    st.table(categories)

    st.subheader("🔢 IPO Financials Calculator")

    col1, col2, col3 = st.columns(3)
    with col1:
        fresh_shares = st.number_input("Fresh Issue Shares (Lakh)", value=100.0)
        ofs_shares = st.number_input("OFS Shares (Lakh)", value=50.0)
    with col2:
        issue_price = st.number_input("Issue Price (₹)", value=500.0)
        flotation_pct = st.number_input("Flotation / Issue Cost (%)", value=3.0)
    with col3:
        pre_ipo_shares = st.number_input("Pre-IPO Shares Outstanding (Lakh)", value=400.0)

    total_issue = (fresh_shares + ofs_shares) * 100000  # convert to actual shares
    fresh_amt = fresh_shares * 100000 * issue_price
    ofs_amt = ofs_shares * 100000 * issue_price
    total_amt = fresh_amt + ofs_amt
    flotation_cost = total_amt * flotation_pct / 100
    net_proceeds_company = fresh_amt - (fresh_amt / total_amt * flotation_cost)

    post_ipo_shares = (pre_ipo_shares + fresh_shares) * 100000

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Issue Size", currency(total_amt))
    with col2:
        st.metric("Net Proceeds to Company", currency(net_proceeds_company))
    with col3:
        st.metric("OFS Proceeds (to sellers)", currency(ofs_amt))
    with col4:
        st.metric("Public Float %", pct(fresh_shares / (pre_ipo_shares + fresh_shares) * 100))

    st.info(f"""
**Promoter Dilution:** Post-IPO, promoters hold
{pct((pre_ipo_shares)/(pre_ipo_shares + fresh_shares)*100)} of shares
(from 100% pre-IPO).
SEBI requires minimum public float of 25%.
""")

# =========================================================
# IPO PRICING & BOOK BUILDING
# =========================================================

elif menu == "IPO Pricing & Book Building":

    st.header("📊 IPO Pricing & Book Building Process")

    st.markdown("""
## What is Book Building?

Book building is the process by which an IPO price is **determined by actual demand**
from investors, rather than fixed upfront.

- A **price band** is set (floor price to cap price)
- Investors bid within the band
- **Cut-off price** = price at which issue is fully subscribed
- Usually the cap of the band for popular IPOs

## Book Building vs Fixed Price Method

| Feature | Book Building | Fixed Price |
|---|---|---|
| Price | Determined by bidding | Fixed upfront |
| Demand discovery | Real-time | Estimated |
| Subscription info | Published daily | After close |
| QIB participation | 50% minimum | Lower |
| Better price discovery | ✅ Yes | ❌ No |
| Used for | Most modern IPOs | Small IPOs |
""")

    st.subheader("🔢 Book Building Simulator")

    col1, col2 = st.columns(2)
    with col1:
        floor_price = st.number_input("Floor Price (₹)", value=450.0)
        cap_price = st.number_input("Cap Price (₹)", value=500.0)
        total_shares_offered = st.number_input("Total Shares Offered (Lakh)", value=100.0)

    with col2:
        st.markdown("**Investor Bids at each price level:**")

    # Simulate demand
    price_levels = np.arange(floor_price, cap_price + 10, 10)
    # Demand decreasing with price (realistic)
    base_demand = total_shares_offered * 3  # oversubscription
    demands = [base_demand * (1 - 0.15 * i) for i in range(len(price_levels))]
    demands = [max(d, total_shares_offered * 0.5) for d in demands]

    # Find cut-off price (highest price where cumulative demand >= total offered)
    cut_off = cap_price
    for i, (price, demand) in enumerate(zip(price_levels, demands)):
        if demand >= total_shares_offered:
            cut_off = price

    demand_df = pd.DataFrame({
        "Price (₹)": price_levels,
        "Demand at this price (Lakh shares)": [round(d, 2) for d in demands],
        "Subscription (x)": [round(d/total_shares_offered, 2) for d in demands]
    })
    st.dataframe(demand_df, use_container_width=True)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=price_levels, y=demands, name="Demand",
                         marker_color='#6B2137'))
    fig.add_hline(y=total_shares_offered, line_dash="dash", line_color="green",
                  annotation_text=f"Issue Size ({total_shares_offered}L shares)")
    fig.add_vline(x=cut_off, line_dash="dot", line_color="gold",
                  annotation_text=f"Cut-off = ₹{cut_off}")
    fig.update_layout(title="Book Building — Demand at Each Price Level",
                      xaxis_title="Bid Price (₹)", yaxis_title="Shares Demanded (Lakh)")
    st.plotly_chart(fig, use_container_width=True)

    st.success(f"**Cut-off Price = ₹{cut_off}**")
    st.info("""
**How allotment works at cut-off:**
- Investors who bid at or above cut-off price get allotment
- If oversubscribed: proportionate allotment for QIB/NII; lottery for Retail
- Investors who bid below cut-off get full refund
""")

    st.subheader("📐 Green Shoe Option (Price Stabilisation)")
    st.info("""
**Green Shoe Option (GSO):**
- BRLMs get option to allot up to **15% additional shares** (over-allotment)
- If share price falls post-listing: BRLM buys shares from market → supports price
- If price holds: exercise green shoe option (issue extra shares at issue price)
- Named after Green Shoe Manufacturing Company (first company to use it)
- In India: SEBI allows GSO for price stabilisation for up to 30 days post-listing
""")

# =========================================================
# IPO VALUATION METHODS
# =========================================================

elif menu == "IPO Valuation Methods":

    st.header("💰 IPO Valuation Methods")

    st.markdown("""
## How is IPO Price Determined?

The issue price is based on **company valuation**, which investment bankers determine using multiple methods:
""")

    method = st.radio("Choose Valuation Method",
                      ["P/E Multiple Method",
                       "EV/EBITDA Method",
                       "Price to Book (P/B) Method",
                       "Discounted Cash Flow (DCF)",
                       "Comparable Company Analysis"])

    if method == "P/E Multiple Method":

        st.markdown("""
$$\\text{Issue Price} = EPS \\times P/E_{\\text{industry}}$$

Most common for profitable companies.
""")
        col1, col2, col3 = st.columns(3)
        with col1:
            eps = st.number_input("EPS (₹)", value=20.0)
        with col2:
            pe_industry = st.number_input("Industry P/E", value=25.0)
        with col3:
            discount = st.number_input("IPO Discount to Industry (%)", value=10.0)

        fair_value = eps * pe_industry
        issue_price_pe = fair_value * (1 - discount/100)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Fair Value (EPS × P/E)", currency(fair_value))
        with col2:
            st.metric("IPO Issue Price (after discount)", currency(issue_price_pe))

        st.info(f"IPOs are typically priced at a **{discount}% discount** to intrinsic value to ensure oversubscription and listing gains.")

    elif method == "EV/EBITDA Method":

        st.markdown("""
$$EV = EBITDA \\times EV/EBITDA_{\\text{industry}}$$

$$\\text{Equity Value} = EV - \\text{Net Debt}$$

$$\\text{Price per Share} = \\frac{\\text{Equity Value}}{\\text{Shares Outstanding}}$$
""")
        col1, col2, col3 = st.columns(3)
        with col1:
            ebitda = st.number_input("EBITDA (₹ Cr)", value=500.0)
            ev_mult = st.number_input("Industry EV/EBITDA", value=12.0)
        with col2:
            net_debt = st.number_input("Net Debt (₹ Cr)", value=200.0)
            shares_ev = st.number_input("Shares Outstanding (Cr)", value=10.0)
        with col3:
            disc_ev = st.number_input("IPO Discount (%)", value=10.0)

        ev = ebitda * ev_mult
        equity_val = ev - net_debt
        price_per_share = equity_val / shares_ev if shares_ev > 0 else 0
        issue_price_ev = price_per_share * (1 - disc_ev/100)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Enterprise Value", f"₹{ev} Cr")
        with col2:
            st.metric("Equity Value", f"₹{equity_val} Cr")
        with col3:
            st.metric("Fair Value/Share", currency(price_per_share))
        with col4:
            st.metric("IPO Price (discounted)", currency(issue_price_ev))

    elif method == "Price to Book (P/B) Method":

        st.markdown("""
$$\\text{Issue Price} = \\text{Book Value per Share} \\times P/B_{\\text{industry}}$$

Used for **banking and financial services** IPOs (HDFC Bank, Kotak, etc.)
""")
        col1, col2 = st.columns(2)
        with col1:
            bvps = st.number_input("Book Value per Share (₹)", value=150.0)
            pb_ind = st.number_input("Industry P/B", value=3.5)
        with col2:
            disc_pb = st.number_input("IPO Discount (%)", value=5.0)

        fair_pb = bvps * pb_ind
        issue_pb = fair_pb * (1 - disc_pb/100)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Fair Value (BVPS × P/B)", currency(fair_pb))
        with col2:
            st.metric("IPO Issue Price", currency(issue_pb))

    elif method == "Discounted Cash Flow (DCF)":

        st.markdown("""
$$\\text{Intrinsic Value} = \\sum_{t=1}^{n} \\frac{FCF_t}{(1+WACC)^t} + \\frac{TV}{(1+WACC)^n}$$

$$\\text{Terminal Value} = \\frac{FCF_n(1+g)}{WACC - g}$$
""")
        col1, col2 = st.columns(2)
        with col1:
            wacc_dcf = st.number_input("WACC (%)", value=12.0)
            g_term = st.number_input("Terminal Growth Rate (%)", value=5.0)
            shares_dcf = st.number_input("Shares Outstanding (Cr)", value=10.0)
            net_debt_dcf = st.number_input("Net Debt (₹ Cr)", value=100.0)
        with col2:
            n_dcf = int(st.number_input("Forecast Years", value=5, min_value=1, step=1))
            fcfs_dcf = []
            for i in range(1, n_dcf+1):
                fcf = st.number_input(f"FCF Year {i} (₹ Cr)", value=100.0+i*20, key=f"dcf_fcf_{i}")
                fcfs_dcf.append(fcf)

        r = wacc_dcf/100
        pv_fcfs = sum(fcf/(1+r)**t for t, fcf in enumerate(fcfs_dcf, 1))
        tv = fcfs_dcf[-1]*(1+g_term/100)/(r - g_term/100) if r > g_term/100 else 0
        pv_tv = tv/(1+r)**n_dcf
        ev_dcf = pv_fcfs + pv_tv
        equity_dcf = ev_dcf - net_debt_dcf
        intrinsic = equity_dcf/shares_dcf if shares_dcf > 0 else 0

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("PV of FCFs", f"₹{round(pv_fcfs,2)} Cr")
        with col2:
            st.metric("PV of Terminal Value", f"₹{round(pv_tv,2)} Cr")
        with col3:
            st.metric("Intrinsic Value per Share", currency(intrinsic))

    elif method == "Comparable Company Analysis":
        st.markdown("""
**Comps Analysis** values the company relative to similar listed peers.

Steps:
1. Select comparable publicly listed companies (same sector, size)
2. Calculate trading multiples (P/E, EV/EBITDA, P/S, P/B)
3. Apply median/mean multiple to target company's metrics
4. Apply an **IPO discount** (typically 10–20%) for liquidity/uncertainty premium
""")

        n_comps = int(st.number_input("Number of Comparables", value=4, min_value=2, max_value=6, step=1))
        target_ebitda = st.number_input("Target Company EBITDA (₹ Cr)", value=300.0)

        comp_data = []
        cols = st.columns(n_comps)
        for i in range(n_comps):
            with cols[i]:
                name = st.text_input("Company", value=f"Comp {i+1}", key=f"comp_name_{i}")
                ev_mult_c = st.number_input("EV/EBITDA", value=10.0 + i*1.5, key=f"comp_mult_{i}")
                comp_data.append({"Company": name, "EV/EBITDA": ev_mult_c})

        df_comps = pd.DataFrame(comp_data)
        median_mult = df_comps["EV/EBITDA"].median()
        mean_mult = df_comps["EV/EBITDA"].mean()

        st.dataframe(df_comps, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Median EV/EBITDA", round(median_mult, 2))
        with col2:
            st.metric("Implied EV of Target", f"₹{round(median_mult * target_ebitda, 2)} Cr")

# =========================================================
# FPO
# =========================================================

elif menu == "Follow-on Public Offer (FPO)":

    st.header("📢 Follow-on Public Offer (FPO)")

    st.markdown("""
## What is an FPO?

An **FPO** is when an **already listed company** issues additional shares to the public.

## Types of FPO

| Type | Description | Cash to Company? |
|---|---|---|
| **Dilutive FPO** | Company issues new shares | ✅ Yes |
| **Non-dilutive FPO** | Existing shareholders sell (OFS) | ❌ No (goes to sellers) |

## FPO vs IPO

| Feature | IPO | FPO |
|---|---|---|
| First-time listing? | ✅ Yes | ❌ No (already listed) |
| Market price exists? | ❌ No | ✅ Yes (reference price) |
| Pricing method | Book building / Fixed | Discount to CMP |
| Regulation | Stricter (DRHP review) | Relatively simpler |
| Typical discount | 10–20% | 5–10% to CMP |
| Examples | Zomato, LIC, Paytm | NTPC, SBI, PFC |
""")

    st.subheader("🔢 FPO Pricing Calculator")

    col1, col2, col3 = st.columns(3)
    with col1:
        cmp = st.number_input("Current Market Price CMP (₹)", value=500.0)
        discount_fpo = st.number_input("FPO Discount to CMP (%)", value=7.0)
    with col2:
        new_shares_fpo = st.number_input("New Shares to Issue (Lakh)", value=200.0)
        pre_shares_fpo = st.number_input("Existing Shares (Lakh)", value=1000.0)
    with col3:
        flotation_fpo = st.number_input("Flotation Cost (%)", value=2.0)

    issue_price_fpo = cmp * (1 - discount_fpo/100)
    gross_proceeds = new_shares_fpo * 100000 * issue_price_fpo
    net_proceeds_fpo = gross_proceeds * (1 - flotation_fpo/100)

    post_shares = pre_shares_fpo + new_shares_fpo
    dilution_pct = new_shares_fpo / post_shares * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("FPO Issue Price", currency(issue_price_fpo))
    with col2:
        st.metric("Gross Proceeds", currency(gross_proceeds))
    with col3:
        st.metric("Net Proceeds (after costs)", currency(net_proceeds_fpo))
    with col4:
        st.metric("Dilution of Existing Holders", pct(dilution_pct))

    st.warning(f"""
**Existing shareholder impact:**
- Pre-FPO CMP = ₹{cmp}
- FPO price = ₹{round(issue_price_fpo,2)} ({round(discount_fpo,1)}% discount)
- Dilution = {round(dilution_pct,2)}% of shares
- New shares increase supply → potential downward price pressure
""")

# =========================================================
# RIGHTS ISSUE
# =========================================================

elif menu == "Rights Issue":

    st.header("📜 Rights Issue")

    st.markdown("""
## What is a Rights Issue?

A **Rights Issue** gives **existing shareholders the right** (but not obligation)
to purchase additional new shares at a **discounted price**, in proportion to their existing holding.

## Key Formula

$$\\text{Rights Ratio} = \\frac{\\text{New shares}}{\\text{Existing shares}} = m : n$$

$$\\text{Theoretical Ex-Rights Price (TERP)} = \\frac{n \\times CMP + m \\times \\text{Issue Price}}{n + m}$$

$$\\text{Value of 1 Right} = CMP - TERP = \\frac{n(CMP - \\text{Issue Price})}{n + m}$$
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        cmp_ri = st.number_input("Current Market Price CMP (₹)", value=500.0)
        issue_price_ri = st.number_input("Rights Issue Price (₹)", value=350.0)
    with col2:
        n_rights = st.number_input("Existing Shares (n)", value=5.0, help="For every n shares held")
        m_rights = st.number_input("New Rights Shares (m)", value=1.0, help="Get m new shares")
    with col3:
        existing_shares_ri = st.number_input("Total Existing Shares (Lakh)", value=100.0)

    terp = (n_rights * cmp_ri + m_rights * issue_price_ri) / (n_rights + m_rights)
    value_of_right = cmp_ri - terp
    theoretical_value_alt = (cmp_ri - issue_price_ri) * m_rights / (n_rights + m_rights)

    new_shares_ri = existing_shares_ri * m_rights / n_rights
    total_proceeds = new_shares_ri * 100000 * issue_price_ri

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("TERP", currency(terp))
    with col2:
        st.metric("Value of 1 Right (₹)", round(value_of_right, 4))
    with col3:
        st.metric("New Shares (Lakh)", round(new_shares_ri, 2))
    with col4:
        st.metric("Total Proceeds", currency(total_proceeds))

    st.success(f"""
**TERP = [{n_rights}×{cmp_ri} + {m_rights}×{issue_price_ri}] / [{n_rights}+{m_rights}]
= {round(terp,4)}**
""")

    st.subheader("📊 Shareholder Options Analysis")

    wealth_subscribe = n_rights * cmp_ri + m_rights * issue_price_ri - (n_rights + m_rights) * terp
    wealth_sell_rights = n_rights * cmp_ri + m_rights * value_of_right - n_rights * terp
    wealth_do_nothing = n_rights * terp - n_rights * cmp_ri  # loss if rights expire

    options_df = pd.DataFrame({
        "Action": [
            "Subscribe (exercise rights)",
            "Sell the rights",
            "Do nothing (let rights lapse)"
        ],
        "Wealth Impact": [
            "No gain, no loss (TERP reflects dilution)",
            "Receive right value = compensated for dilution",
            f"LOSS = ₹{round(abs(wealth_do_nothing),2)} per {n_rights} shares (rights worth forfeited)"
        ],
        "Recommendation": ["✅ Preferred if cash available", "✅ If no cash", "❌ Avoidable loss"]
    })
    st.table(options_df)

    st.subheader("📘 Excel Formula")
    st.code(f"=({n_rights}*CMP + {m_rights}*Issue_Price)/({n_rights}+{m_rights})", language="excel")

# =========================================================
# BONUS ISSUE
# =========================================================

elif menu == "Bonus Issue":

    st.header("🎁 Bonus Issue (Stock Dividend / Capitalisation Issue)")

    st.markdown("""
## What is a Bonus Issue?

A **bonus issue** (also called **stock dividend** or **capitalisation issue**) is when
a company issues **free additional shares** to existing shareholders, in proportion to their holdings.

## Key Characteristics
- **No cash is raised** — it's a transfer from reserves to paid-up capital
- Share price **adjusts downward** proportionally
- Total shareholder wealth **does not change** (theoretically)
- Signals management's **confidence** in the company
- Improves **market liquidity** by increasing share count and reducing per-share price

## Formula

$$\\text{Bonus Ratio} = p : q \\text{ (p new shares for every q existing)}$$

$$\\text{Ex-Bonus Price} = \\frac{CMP \\times q}{p + q}$$

$$\\text{Total Shares After} = \\text{Existing Shares} \\times \\left(1 + \\frac{p}{q}\\right)$$
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        cmp_bonus = st.number_input("Current Market Price (₹)", value=1000.0)
    with col2:
        p_bonus = st.number_input("Bonus Shares (p) per q existing", value=1.0)
        q_bonus = st.number_input("Existing Shares (q)", value=1.0)
    with col3:
        existing_bonus = st.number_input("Total Existing Shares (Lakh)", value=50.0)

    ex_bonus_price = cmp_bonus * q_bonus / (p_bonus + q_bonus)
    new_shares_bonus = existing_bonus * p_bonus / q_bonus
    total_after = existing_bonus + new_shares_bonus

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Ex-Bonus Price", currency(ex_bonus_price))
    with col2:
        st.metric("Price Drop", currency(cmp_bonus - ex_bonus_price))
    with col3:
        st.metric("New Shares Issued (Lakh)", round(new_shares_bonus, 2))
    with col4:
        st.metric("Total Shares After (Lakh)", round(total_after, 2))

    # Shareholder wealth check
    pre_wealth = existing_bonus * cmp_bonus
    post_wealth = total_after * ex_bonus_price
    st.info(f"""
**Wealth check:**
- Pre-bonus wealth = {existing_bonus}L × ₹{cmp_bonus} = ₹{round(pre_wealth,0):,}
- Post-bonus wealth = {round(total_after,2)}L × ₹{round(ex_bonus_price,2)} = ₹{round(post_wealth,0):,}
- **No change in wealth — bonus issue is a cosmetic accounting adjustment**
""")

    st.subheader("Accounting Treatment")
    accounting = pd.DataFrame({
        "Account": ["Securities Premium Reserve", "General Reserves", "Paid-up Share Capital"],
        "Effect": [
            "Debited (used to fund bonus)",
            "Debited (used to fund bonus)",
            "Credited (increased by bonus shares × face value)"
        ],
        "Note": [
            "SEBI allows bonus from free reserves, securities premium",
            "Companies prefer to maintain some reserves",
            "Share capital increases; total equity unchanged"
        ]
    })
    st.table(accounting)

    st.warning("""
**EPS Impact of Bonus Issue:**
EPS falls proportionally because the same earnings are now spread over more shares.
P/E ratio remains the same (numerator and denominator both fall/rise proportionally).
""")

    new_ipo_eps = st.number_input("Current EPS (₹)", value=50.0)
    adj_eps = new_ipo_eps * q_bonus / (p_bonus + q_bonus)
    st.metric("Adjusted EPS after bonus", currency(adj_eps))

# =========================================================
# PRIVATE PLACEMENT
# =========================================================

elif menu == "Private Placement":

    st.header("🤝 Private Placement")

    st.markdown("""
## What is Private Placement?

A **private placement** is the sale of shares (or securities) to a **select group of investors**
rather than the general public.

## Types (Under Companies Act 2013)

| Type | Who Can Invest | Max Investors | SEBI Approval? |
|---|---|---|---|
| **Private Placement** | Select identified persons | 200 in a FY | No public filing |
| **Preferential Allotment** | Specific entities/persons | No limit | SEBI approval (listed) |
| **QIP** | Qualified Institutional Buyers | No limit | Simpler SEBI process |

## Key Characteristics
- **No public offer** — not advertised to general public
- Faster than IPO/FPO (no SEBI DRHP review)
- **Private companies** use this for pre-IPO funding
- Typically at **negotiated price** (can be discount or premium)
- Investors receive **information rights, board seats** as part of negotiation
""")

    st.subheader("🔢 Private Placement Calculator")

    col1, col2, col3 = st.columns(3)
    with col1:
        pre_money_val = st.number_input("Pre-money Valuation (₹ Cr)", value=500.0)
        investment = st.number_input("Investment Amount (₹ Cr)", value=100.0)
    with col2:
        pre_shares_pp = st.number_input("Pre-investment Shares (Lakh)", value=100.0)
    with col3:
        st.markdown("**Derived:**")

    post_money = pre_money_val + investment
    price_per_share = pre_money_val / (pre_shares_pp * 100000) * 100000  # ₹ per share
    new_shares_pp = investment * 100 / price_per_share  # in lakh shares (both in Cr/lakh scale)
    # Simplify: new_shares (lakh) = Investment_Cr / pre_money_Cr * pre_shares_lakh
    new_shares_pp = (investment / pre_money_val) * pre_shares_pp / (1 - investment/post_money)
    # Correct approach:
    new_shares_pp = pre_shares_pp * investment / pre_money_val
    investor_stake = new_shares_pp / (pre_shares_pp + new_shares_pp) * 100

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Post-money Valuation", f"₹{round(post_money,2)} Cr")
    with col2:
        st.metric("Price per Share", currency(pre_money_val*1e6 / (pre_shares_pp*100000) if pre_shares_pp > 0 else 0))
    with col3:
        st.metric("New Shares (Lakh)", round(new_shares_pp, 4))
    with col4:
        st.metric("Investor Stake", pct(investor_stake))

    st.info(f"""
**Pre-money / Post-money:**
- Pre-money = Company value BEFORE investment = ₹{pre_money_val} Cr
- Investment = ₹{investment} Cr
- Post-money = ₹{round(post_money,2)} Cr
- Investor owns {round(investor_stake,2)}% = Investment / Post-money = {investment}/{round(post_money,2)}
""")

# =========================================================
# QIP
# =========================================================

elif menu == "Qualified Institutional Placement (QIP)":

    st.header("🏦 Qualified Institutional Placement (QIP)")

    st.markdown("""
## What is a QIP?

A **QIP** is a fast-track equity issuance mechanism that allows **listed companies**
to raise capital from **Qualified Institutional Buyers (QIBs)** without going through
the lengthy public offering process.

## Key Features (SEBI Regulations)

| Parameter | Requirement |
|---|---|
| Eligible issuers | Listed companies only |
| Eligible investors | QIBs only (FIIs, Mutual Funds, Banks, Insurance) |
| Minimum price | Floor price based on 2-week average CMP |
| Discount allowed | Up to 5% below floor price |
| Maximum shares | 5 times paid-up capital in 12 months |
| Lock-in period | 1 year for shares allotted |
| Time to complete | 3–7 days (vs 4–6 months for FPO) |
| Board resolution | Required (no shareholder approval usually) |
""")

    st.subheader("🔢 QIP Pricing Calculator")

    col1, col2 = st.columns(2)
    with col1:
        prices_14d = []
        for i in range(1, 15):
            prices_14d.append(490 + random.uniform(-20, 20))

        st.markdown("**14 trading days closing prices (auto-simulated):**")
        avg_14d = np.mean(prices_14d)
        st.metric("14-Day Average Price", currency(avg_14d))

        cmp_qip = st.number_input("Current Market Price CMP (₹)", value=500.0)
        wap_26w = st.number_input("26-week WAP (₹)", value=480.0)

    with col2:
        floor_qip = max(avg_14d, wap_26w)
        discount_qip = st.number_input("QIP Discount from Floor (%)", value=3.0, max_value=5.0)
        issue_price_qip = floor_qip * (1 - discount_qip/100)

        raise_amount = st.number_input("Amount to Raise (₹ Cr)", value=500.0)

    shares_to_issue = raise_amount * 1e7 / issue_price_qip / 1e5  # in lakh shares

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Floor Price", currency(floor_qip))
    with col2:
        st.metric("QIP Issue Price", currency(issue_price_qip))
    with col3:
        st.metric("Shares to Issue (Lakh)", round(shares_to_issue, 2))

    st.subheader("QIP vs FPO vs Rights Issue")

    comparison_qip = pd.DataFrame({
        "Feature": ["Time to complete", "Investor type", "SEBI approval", "Discount typical",
                    "Shareholder approval", "Use when"],
        "QIP": ["3-7 days", "QIBs only", "Simple filings", "3-5%", "Board only",
                "Emergency capital need; market window"],
        "FPO": ["3-6 months", "All investors", "Full review", "5-10%", "Required",
                "Larger capital raise; brand visibility"],
        "Rights Issue": ["2-4 months", "Existing shareholders", "SEBI approval", "20-40%",
                         "Required", "Protect existing ownership; rights"]
    })
    st.table(comparison_qip)

# =========================================================
# PREFERENTIAL ALLOTMENT
# =========================================================

elif menu == "Preferential Allotment":

    st.header("📋 Preferential Allotment")

    st.markdown("""
## What is Preferential Allotment?

A **preferential allotment** is the issue of shares (or convertible securities) to a
**specific set of identified investors** (not the general public) at a price decided by the board.

## SEBI Rules for Preferential Allotment (Listed Companies)

- **Shareholder approval** required (special resolution — 75% votes)
- **Minimum price** = Higher of:
  - Floor price based on 26-week average CMP
  - Floor price based on 2-week average CMP
- **Lock-in:** Allottees (promoters: 3 years; others: 1 year)
- Used for: strategic investor entry, promoter stake increase, FII entry, restructuring

## Formula — Minimum Issue Price (SEBI)

$$\\text{Floor Price} = \\text{Higher of (26-week WAP, 2-week average)}$$
""")

    col1, col2 = st.columns(2)
    with col1:
        wap_26w_pa = st.number_input("26-week Weighted Average Price (₹)", value=480.0)
        avg_2w_pa = st.number_input("2-week Average Price (₹)", value=495.0)
    with col2:
        pref_shares = st.number_input("Shares to Allot (Lakh)", value=50.0)

    floor_pa = max(wap_26w_pa, avg_2w_pa)
    proceeds_pa = pref_shares * 100000 * floor_pa

    col1, col2 = st.columns(2)
    with col1:
        st.metric("SEBI Floor Price", currency(floor_pa))
    with col2:
        st.metric("Minimum Proceeds", currency(proceeds_pa))

    st.success(f"Floor Price = max(₹{wap_26w_pa}, ₹{avg_2w_pa}) = ₹{floor_pa}")

    st.subheader("Use Cases")
    use_cases = [
        "**Strategic investor entry:** Foreign company takes stake in Indian listed firm",
        "**Promoter stake increase:** Promoters increase their holding via preferential allotment",
        "**FII / PE entry:** Large institutional investor takes direct stake",
        "**Conversion of debt:** Lender converts loans into equity (debt restructuring)",
        "**Anchor investor pre-IPO:** Large investor takes stake before IPO",
    ]
    for u in use_cases:
        st.markdown(f"- {u}")

# =========================================================
# VENTURE CAPITAL
# =========================================================

elif menu == "Venture Capital (VC)":

    st.header("🚀 Venture Capital (VC) Funding")

    st.markdown("""
## What is Venture Capital?

**Venture Capital (VC)** is private equity investment in **early-stage, high-growth startups**
that have high potential but also high risk.

## VC Funding Rounds
""")

    vc_rounds = pd.DataFrame({
        "Round": ["Pre-Seed / Bootstrapping", "Seed Round", "Series A", "Series B", "Series C+", "Pre-IPO / Growth"],
        "Stage": ["Idea/MVP", "Product-Market Fit", "Scale", "Expand", "Dominate market", "Pre-listing"],
        "Typical Raise (India)": ["₹10L–₹1Cr", "₹1–10 Cr", "₹10–100 Cr", "₹100–500 Cr",
                                   "₹500Cr+", "₹500Cr–2000Cr"],
        "Investors": ["Founders, F&F", "Angel Investors", "VC Funds", "VC + PE", "PE + Strategics", "PE + Institutional"],
        "Dilution Typical": ["N/A", "10–20%", "20–25%", "15–20%", "10–15%", "5–15%"],
        "Examples": ["Zepto founder-funded initially",
                     "CRED seed (Sequoia)", "Meesho Series A",
                     "Nykaa Series B", "Swiggy Series C+",
                     "Zomato pre-IPO rounds"]
    })
    st.table(vc_rounds)

    st.subheader("🔢 VC Dilution & Ownership Calculator")

    st.markdown("**Track ownership across multiple rounds:**")

    col1, col2 = st.columns(2)
    with col1:
        founders_initial = st.number_input("Founder Ownership Start (%)", value=100.0)
        n_rounds = int(st.number_input("Number of Funding Rounds", value=3, min_value=1, max_value=5, step=1))

    rounds_data = []
    cols = st.columns(n_rounds)
    for i in range(n_rounds):
        with cols[i]:
            round_name = st.text_input("Round", value=f"Series {chr(65+i)}", key=f"vc_rname_{i}")
            dilution = st.number_input("Dilution (%)", value=20.0 - i*3, key=f"vc_dil_{i}")
            invest = st.number_input("Investment (₹ Cr)", value=50.0*(i+1), key=f"vc_inv_{i}")
            rounds_data.append({"Round": round_name, "Dilution (%)": dilution, "Investment (₹ Cr)": invest})

    # Track founder stake
    current_stake = founders_initial
    ownership_track = [{"Round": "Start", "Founder %": current_stake, "Cumulative Raised": 0}]
    cumulative = 0
    for rd in rounds_data:
        current_stake = current_stake * (1 - rd["Dilution (%)"]/100)
        cumulative += rd["Investment (₹ Cr)"]
        ownership_track.append({"Round": rd["Round"],
                                  "Founder %": round(current_stake, 2),
                                  "Cumulative Raised": cumulative})

    df_ownership = pd.DataFrame(ownership_track)
    st.dataframe(df_ownership, use_container_width=True)

    fig = go.Figure()
    fig.add_trace(go.Bar(x=df_ownership["Round"], y=df_ownership["Founder %"],
                         marker_color='#6B2137', name='Founder Ownership %'))
    fig.update_layout(title="Founder Ownership Dilution Across Rounds",
                      xaxis_title="Round", yaxis_title="Founder Stake (%)")
    st.plotly_chart(fig, use_container_width=True)

    st.success(f"After all rounds: Founder owns **{round(current_stake,2)}%** and raised **₹{cumulative} Cr**")

# =========================================================
# PRIVATE EQUITY
# =========================================================

elif menu == "Private Equity (PE)":

    st.header("💼 Private Equity (PE)")

    st.markdown("""
## VC vs Private Equity

| Feature | Venture Capital (VC) | Private Equity (PE) |
|---|---|---|
| Stage | Early-stage startups | Mature, established firms |
| Risk | Very high | Moderate to high |
| Return target | 10x–100x | 2x–5x |
| Investment horizon | 5–10 years | 3–7 years |
| Typical investment | Minority stake | Majority or control stake |
| Involvement | Board seat, mentoring | Operational restructuring |
| Exit routes | IPO, M&A | IPO, strategic sale, secondary |
| Examples India | Sequoia, Accel | KKR, Blackstone, Carlyle |

## PE Investment Structures
""")

    pe_structures = pd.DataFrame({
        "Structure": ["Growth Equity", "Leveraged Buyout (LBO)", "Buyout", "PIPE", "Venture Debt"],
        "Description": [
            "PE invests in fast-growing firms; minority stake",
            "PE acquires company using significant debt",
            "PE takes majority or full control; restructures",
            "Public Investment in Private Equity — PE buys discounted listed shares",
            "Debt with equity warrants; used alongside VC"
        ],
        "When Used": [
            "Profitable firm needs capital for expansion",
            "PE sees value in mature underperforming firm",
            "Family business succession; conglomerate divestitures",
            "Distressed listed companies; deep discount entry",
            "Startups between equity rounds"
        ]
    })
    st.table(pe_structures)

    st.subheader("🔢 LBO Return Calculator")

    st.markdown("""
**Leveraged Buyout (LBO):**
PE acquires a company using **mostly debt** (60–80%), with smaller equity contribution.
Returns are amplified by financial leverage.
""")

    col1, col2 = st.columns(2)
    with col1:
        enterprise_value = st.number_input("Acquisition EV (₹ Cr)", value=1000.0)
        debt_pct_lbo = st.number_input("Debt as % of EV", value=65.0)
        holding_years = st.number_input("Holding Period (Years)", value=5.0)
    with col2:
        exit_ev_multiple = st.number_input("Exit EV/EBITDA Multiple", value=12.0)
        entry_ev_multiple = st.number_input("Entry EV/EBITDA Multiple", value=8.0)
        ebitda_growth = st.number_input("Annual EBITDA Growth (%)", value=15.0)
        ebitda_entry = st.number_input("Entry EBITDA (₹ Cr)", value=125.0)

    debt_lbo = enterprise_value * debt_pct_lbo / 100
    equity_lbo = enterprise_value - debt_lbo

    ebitda_exit = ebitda_entry * (1 + ebitda_growth/100) ** holding_years
    exit_ev = ebitda_exit * exit_ev_multiple
    debt_remaining = debt_lbo * 0.5  # assume 50% repaid
    exit_equity = exit_ev - debt_remaining

    moic = exit_equity / equity_lbo if equity_lbo > 0 else 0  # Multiple on Invested Capital
    irr_lbo = (moic ** (1/holding_years) - 1) * 100 if moic > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Equity Invested", f"₹{round(equity_lbo,2)} Cr")
    with col2:
        st.metric("Exit Equity Value", f"₹{round(exit_equity,2)} Cr")
    with col3:
        st.metric("MOIC", f"{round(moic,2)}x")
    with col4:
        st.metric("Implied IRR", pct(irr_lbo))

# =========================================================
# ESOP
# =========================================================

elif menu == "ESOP (Employee Stock Options)":

    st.header("👷 Employee Stock Option Plan (ESOP)")

    st.markdown("""
## What is an ESOP?

An **ESOP** grants employees the **right to purchase company shares** at a
**pre-determined exercise price** (grant price) after a vesting period.

## Key Terms

| Term | Definition |
|---|---|
| **Grant Date** | Date on which options are granted to employee |
| **Grant Price** | Price at which employee can buy shares (usually CMP at grant) |
| **Vesting Period** | Time before options can be exercised (typically 1–4 years) |
| **Exercise Period** | Window to exercise after vesting |
| **Cliff Vesting** | All options vest at once after minimum period |
| **Graded Vesting** | Options vest gradually (e.g. 25% per year over 4 years) |

## Formula

$$\\text{Gain per Option} = \\text{Market Price at Exercise} - \\text{Grant Price}$$

$$\\text{Total ESOP Value} = \\text{No. of Options} \\times \\text{Gain per Option}$$
""")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        grant_price = st.number_input("Grant Price (₹)", value=100.0)
    with col2:
        market_price = st.number_input("Market Price at Exercise (₹)", value=300.0)
    with col3:
        num_options = st.number_input("Number of Options", value=10000.0)
    with col4:
        tax_esop = st.number_input("Tax Rate on Gain (%)", value=30.0)

    gain_per = market_price - grant_price
    total_gain = num_options * gain_per
    tax_paid = total_gain * tax_esop / 100
    net_gain = total_gain - tax_paid

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Gain per Option", currency(gain_per))
    with col2:
        st.metric("Total Pre-tax Gain", currency(total_gain))
    with col3:
        st.metric("Net Post-tax Gain", currency(net_gain))

    st.subheader("📅 Vesting Schedule Calculator")

    vesting_type = st.radio("Vesting Type", ["Graded (25% per year)", "Cliff (100% after 3 years)",
                                               "Custom"])

    total_options = int(num_options)
    vesting_years = 4

    if vesting_type == "Graded (25% per year)":
        sched = [(f"Year {i+1}", total_options//4) for i in range(4)]
    elif vesting_type == "Cliff (100% after 3 years)":
        sched = [("Year 1", 0), ("Year 2", 0), ("Year 3", total_options)]
    else:
        sched = [(f"Year {i+1}", int(total_options*[0.1, 0.2, 0.3, 0.4][i])) for i in range(4)]

    cumulative = 0
    vest_data = []
    for yr, opts in sched:
        cumulative += opts
        vest_data.append({"Year": yr, "Options Vesting": opts,
                           "Cumulative Vested": cumulative,
                           "Value at Current MP (₹)": opts * gain_per})

    df_vest = pd.DataFrame(vest_data)
    st.dataframe(df_vest, use_container_width=True)

    st.subheader("Taxation of ESOPs in India")
    st.info("""
**India ESOP Tax Treatment (Budget 2021 onwards):**

- **At Exercise:** Difference (Market Price − Grant Price) = **Perquisite** → taxed as salary income
- **At Sale:** Capital gain on (Sale Price − Market Price at exercise)
  - If held < 12 months: **Short-term capital gain** (STCG = 15%)
  - If held ≥ 12 months: **Long-term capital gain** (LTCG = 10% above ₹1L)
- **Startup ESOP Relief:** Tax on perquisite deferred to earliest of — 5 years, exit, or sale
""")

# =========================================================
# CONVERTIBLE INSTRUMENTS
# =========================================================

elif menu == "Convertible Instruments":

    st.header("🔄 Convertible Instruments")

    st.markdown("""
## Types of Convertible Instruments

### 1. Compulsorily Convertible Preference Shares (CCPS)
- Must convert into equity after a specified period
- No fixed redemption — converts automatically
- Common in PE/VC investments in India

### 2. Compulsorily Convertible Debentures (CCD)
- Debentures that MUST convert to equity
- Investors earn interest until conversion
- RBI treats as FDI (Foreign Direct Investment) since they ultimately become equity

### 3. Optionally Convertible Debentures (OCD)
- Investor has the OPTION to convert or redeem

### 4. Warrants
- Right to buy shares at a fixed price in the future
- No immediate dilution until exercised
""")

    st.subheader("🔢 Convertible Security Calculator")

    conv_type = st.radio("Instrument Type", ["CCPS", "CCD", "Warrant"])

    if conv_type in ["CCPS", "CCD"]:

        col1, col2, col3 = st.columns(3)
        with col1:
            invest_conv = st.number_input("Investment Amount (₹ Cr)", value=50.0)
            dividend_rate = st.number_input("Dividend/Coupon Rate (%)", value=8.0 if conv_type=="CCPS" else 10.0)
        with col2:
            pre_money_conv = st.number_input("Pre-money Valuation at Conversion (₹ Cr)", value=400.0)
            conv_years = st.number_input("Years to Conversion", value=3.0)
        with col3:
            conversion_premium = st.number_input("Conversion Premium over Pre-money (%)", value=0.0)

        conversion_val = pre_money_conv * (1 + conversion_premium/100)
        post_money_conv = conversion_val + invest_conv
        stake = invest_conv / post_money_conv * 100

        annual_income = invest_conv * dividend_rate / 100
        total_income_before = annual_income * conv_years

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(f"Annual {'Dividend' if conv_type=='CCPS' else 'Interest'}", f"₹{round(annual_income,2)} Cr")
        with col2:
            st.metric("Total Income Before Conversion", f"₹{round(total_income_before,2)} Cr")
        with col3:
            st.metric("Equity Stake on Conversion", pct(stake))

    else:  # Warrants
        col1, col2 = st.columns(2)
        with col1:
            warrant_price = st.number_input("Exercise Price of Warrant (₹)", value=100.0)
            current_share = st.number_input("Current Share Price (₹)", value=120.0)
            num_warrants = st.number_input("Number of Warrants", value=100000.0)
        with col2:
            expiry_years = st.number_input("Expiry (Years)", value=2.0)

        intrinsic_val = max(current_share - warrant_price, 0)
        total_intrinsic = intrinsic_val * num_warrants

        st.metric("Intrinsic Value per Warrant", currency(intrinsic_val))
        st.metric("Total Intrinsic Value", currency(total_intrinsic))

        if current_share > warrant_price:
            st.success(f"✅ Warrant is IN-THE-MONEY by ₹{round(intrinsic_val,2)} per warrant")
        elif current_share == warrant_price:
            st.info("Warrant is AT-THE-MONEY")
        else:
            st.error(f"❌ Warrant is OUT-OF-THE-MONEY by ₹{round(warrant_price-current_share,2)}")

# =========================================================
# ADR & GDR
# =========================================================

elif menu == "ADR & GDR":

    st.header("🌍 American & Global Depository Receipts (ADR/GDR)")

    st.markdown("""
## What are DRs?

**Depository Receipts (DRs)** allow Indian companies to list and raise equity
from foreign markets without a direct overseas listing.

| Feature | ADR | GDR |
|---|---|---|
| Where listed | US exchanges (NYSE, NASDAQ) | International exchanges (Luxembourg, London) |
| Currency | US Dollars | Usually US Dollars or Euros |
| Regulator | SEC (US Securities & Exchange Commission) | Local exchange rules |
| Investors | US investors primarily | Global institutional investors |
| Popular Indian examples | Infosys, WIPRO, HDFC Bank | Many Indian companies |

## Mechanics

1. Indian company deposits shares with a **domestic custodian bank**
2. Custodian bank issues a **receipt** to foreign depository bank
3. Foreign depository bank issues **ADR/GDR** to foreign investors
4. Each DR = fixed ratio of underlying Indian shares (e.g., 1 ADR = 2 NSE shares)

## DR Ratio & Pricing

$$\\text{ADR Price (USD)} = \\frac{\\text{Indian Share Price (INR)}}{\\text{Exchange Rate}} \\times \\text{DR Ratio}$$
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        indian_price = st.number_input("Indian Share Price (₹)", value=1500.0)
        usd_inr = st.number_input("USD/INR Exchange Rate", value=83.0)
    with col2:
        dr_ratio = st.number_input("DR Ratio (Indian shares per DR)", value=2.0)
    with col3:
        adr_market = st.number_input("ADR Market Price (USD)", value=36.0)

    theoretical_adr = (indian_price / usd_inr) * dr_ratio

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Theoretical ADR Price (USD)", f"${round(theoretical_adr, 2)}")
    with col2:
        st.metric("Actual ADR Market Price (USD)", f"${adr_market}")

    premium = (adr_market - theoretical_adr) / theoretical_adr * 100
    if abs(premium) < 1:
        st.success(f"ADR is fairly priced (difference = {round(premium,2)}%)")
    elif premium > 0:
        st.warning(f"ADR trades at {round(premium,2)}% PREMIUM to theoretical — potential arbitrage")
    else:
        st.info(f"ADR trades at {round(abs(premium),2)}% DISCOUNT to theoretical")

    st.subheader("Benefits of ADR/GDR")
    benefits = [
        "Access to deeper and larger foreign capital markets",
        "Higher valuations possible in US/European markets",
        "Enhanced global visibility and brand recognition",
        "Diversification of investor base",
        "Foreign exchange earnings on capital raised",
        "No direct listing overseas — simpler process",
    ]
    for b in benefits:
        st.markdown(f"- {b}")

# =========================================================
# RETAINED EARNINGS VS NEW EQUITY
# =========================================================

elif menu == "Retained Earnings vs New Equity":

    st.header("📊 Retained Earnings vs New Equity Issue")

    st.markdown("""
## Cost of Retained Earnings vs New Equity

Both represent **equity capital** but differ in cost due to **flotation costs**.

### Cost of Retained Earnings (Ke)

No flotation costs — uses current market price P₀

$$K_{re} = \\frac{D_1}{P_0} + g$$

### Cost of New Equity Issue (Ke_new)

Flotation costs reduce net proceeds → higher effective cost

$$K_{e,new} = \\frac{D_1}{P_0(1-f)} + g$$

Where **f** = flotation cost as % of issue price

### CAPM Approach (same for both — no flotation adjustment)

$$K_e = R_f + \\beta \\times ERP$$
""")

    col1, col2, col3 = st.columns(3)
    with col1:
        d0_re = st.number_input("D₀ — Last Dividend (₹)", value=5.0)
        g_re = st.number_input("Growth Rate g (%)", value=8.0)
    with col2:
        p0_re = st.number_input("Current Market Price P₀ (₹)", value=100.0)
    with col3:
        flotation_re = st.number_input("Flotation Cost f (%)", value=5.0)

    d1_re = d0_re * (1 + g_re/100)
    ke_re = d1_re / p0_re * 100 + g_re
    ke_new = d1_re / (p0_re * (1 - flotation_re/100)) * 100 + g_re
    cost_diff = ke_new - ke_re

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("D₁ = D₀(1+g)", f"₹{round(d1_re,4)}")
    with col2:
        st.metric("Ke (Retained Earnings)", pct(ke_re))
    with col3:
        st.metric("Ke (New Equity Issue)", pct(ke_new))

    st.warning(f"""
**Cost Difference:** New equity costs {round(cost_diff,4)}% MORE than retained earnings
due to flotation costs. This explains why **firms prefer retained earnings** (Pecking Order).
""")

    st.subheader("📊 Impact of Flotation Cost on Ke")

    flotation_range = np.arange(0, 16, 1)
    ke_new_range = [d1_re / (p0_re * (1 - f/100)) * 100 + g_re for f in flotation_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=flotation_range, y=ke_new_range, mode='lines',
                             name='Ke (New Equity)', line=dict(color='#6B2137', width=2)))
    fig.add_hline(y=ke_re, line_dash="dash", line_color="green",
                  annotation_text=f"Ke (Retained Earnings) = {round(ke_re,2)}%")
    fig.update_layout(title="Effect of Flotation Cost on Cost of New Equity",
                      xaxis_title="Flotation Cost (%)", yaxis_title="Cost of Equity (%)")
    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# COST OF NEW EQUITY
# =========================================================

elif menu == "Cost of New Equity (Flotation Costs)":

    st.header("💸 Cost of New Equity with Flotation Costs")

    st.markdown("""
## What are Flotation Costs?

**Flotation costs** are the expenses incurred when issuing new securities:
- Investment banker fees (underwriting)
- Legal and accounting fees
- SEBI filing fees
- Marketing and roadshow expenses
- Typically **2–7% of issue size**

## Formula

$$K_{e,new} = \\frac{D_1}{P_0(1-f)} + g$$

or using CAPM (adjusted):

$$K_{e,new} = R_f + \\beta(R_m - R_f) + \\text{Flotation Adjustment}$$

where Flotation Adjustment = $\\frac{f \\times K_e}{1-f}$
""")

    st.subheader("🔢 Three Approaches")

    approach = st.radio("Approach", ["Gordon Growth + Flotation", "CAPM + Flotation",
                                      "Bond Yield + Risk Premium + Flotation"])

    if approach == "Gordon Growth + Flotation":

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            d0_fc = st.number_input("D₀ (₹)", value=5.0)
        with col2:
            p0_fc = st.number_input("P₀ (₹)", value=100.0)
        with col3:
            g_fc = st.number_input("g (%)", value=8.0)
        with col4:
            f_fc = st.number_input("Flotation Cost f (%)", value=5.0)

        d1_fc = d0_fc*(1+g_fc/100)
        net_p = p0_fc*(1-f_fc/100)
        ke_fc = d1_fc/net_p*100 + g_fc

        st.latex(f"K_e = \\frac{{{round(d1_fc,4)}}}{{{round(net_p,2)}}} + {g_fc}\\% = {round(ke_fc,4)}\\%")
        st.success(f"Ke (New Issue) = {pct(ke_fc)}")

    elif approach == "CAPM + Flotation":

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            rf_fc = st.number_input("Rf (%)", value=7.0)
        with col2:
            beta_fc = st.number_input("Beta", value=1.2)
        with col3:
            erp_fc = st.number_input("ERP (%)", value=6.0)
        with col4:
            f_fc2 = st.number_input("Flotation (%)", value=5.0)

        ke_capm = rf_fc + beta_fc*erp_fc
        flotation_adj = (f_fc2/100 * ke_capm) / (1 - f_fc2/100)
        ke_new_capm = ke_capm + flotation_adj

        col1, col2 = st.columns(2)
        with col1:
            st.metric("CAPM Ke (without flotation)", pct(ke_capm))
        with col2:
            st.metric("Ke (new issue, with flotation)", pct(ke_new_capm))

    else:
        col1, col2, col3 = st.columns(3)
        with col1:
            kd_by = st.number_input("Pre-tax Kd / Bond YTM (%)", value=10.0)
        with col2:
            rp_by = st.number_input("Risk Premium (%)", value=4.0)
        with col3:
            f_by = st.number_input("Flotation (%)", value=5.0)

        ke_bond = kd_by + rp_by
        ke_bond_new = ke_bond / (1 - f_by/100)

        col1, col2 = st.columns(2)
        with col1:
            st.metric("Ke (Bond + RP)", pct(ke_bond))
        with col2:
            st.metric("Ke (adjusted for flotation)", pct(ke_bond_new))

# =========================================================
# DILUTION ANALYSIS
# =========================================================

elif menu == "Dilution Analysis":

    st.header("📉 Dilution Analysis")

    st.markdown("""
## Types of Dilution

| Type | What Dilutes? | Trigger |
|---|---|---|
| **Ownership Dilution** | % stake of existing shareholders | New shares issued |
| **EPS Dilution** | Earnings Per Share | New shares (if earnings don't grow proportionately) |
| **Book Value Dilution** | Book Value Per Share | New shares below current BVPS |
| **Voting Dilution** | Voting power | New shares with voting rights |

## Anti-Dilution Protection (for VC/PE)

Investors often have **anti-dilution clauses** to protect against future rounds at lower valuations (down rounds):
- **Full Ratchet:** Most aggressive — investor's price adjusted to new lower price
- **Weighted Average:** More balanced — adjusted based on number of shares at new price
- **Pay-to-play:** Investor must participate in new round to keep protection
""")

    st.subheader("🔢 Dilution Calculator")

    col1, col2, col3 = st.columns(3)
    with col1:
        pre_shares_dil = st.number_input("Pre-issue Shares (Lakh)", value=100.0)
        pre_price = st.number_input("Current Market Price / BVPS (₹)", value=500.0)
        eps_before = st.number_input("Current EPS (₹)", value=25.0)
    with col2:
        new_shares_dil = st.number_input("New Shares to Issue (Lakh)", value=20.0)
        issue_price_dil = st.number_input("Issue Price of New Shares (₹)", value=450.0)
    with col3:
        new_earnings = st.number_input("Expected Earnings from New Capital (₹ Lakh)", value=80.0,
                                        help="Additional earnings from deployment of raised funds")

    post_shares_dil = pre_shares_dil + new_shares_dil
    total_equity_pre = pre_shares_dil * 100000 * pre_price
    total_equity_post = total_equity_pre + new_shares_dil * 100000 * issue_price_dil

    bvps_post = total_equity_post / (post_shares_dil * 100000)

    total_earnings_before = eps_before * pre_shares_dil * 100000
    total_earnings_after = total_earnings_before + new_earnings * 100000
    eps_after = total_earnings_after / (post_shares_dil * 100000)

    ownership_pre = pre_shares_dil / pre_shares_dil * 100
    ownership_post = pre_shares_dil / post_shares_dil * 100

    dilution_df = pd.DataFrame({
        "Metric": ["Ownership %", "EPS (₹)", "BVPS (₹)", "Shares Outstanding (Lakh)"],
        "Before Issue": [f"{round(ownership_pre,2)}%", f"₹{eps_before}",
                          f"₹{pre_price}", f"{pre_shares_dil}L"],
        "After Issue": [f"{round(ownership_post,2)}%", f"₹{round(eps_after,4)}",
                         f"₹{round(bvps_post,2)}", f"{post_shares_dil}L"],
        "Change": [
            f"−{round(ownership_pre-ownership_post,2)}%",
            f"{'−' if eps_after < eps_before else '+'}₹{abs(round(eps_after-eps_before,4))}",
            f"{'−' if bvps_post < pre_price else '+'}₹{abs(round(bvps_post-pre_price,2))}",
            f"+{new_shares_dil}L"
        ]
    })
    st.table(dilution_df)

    if eps_after >= eps_before:
        st.success("✅ EPS Accretive — New issue increases EPS (new capital earns more than its cost)")
    else:
        st.warning("⚠️ EPS Dilutive — New issue decreases EPS (new capital earnings insufficient)")

# =========================================================
# EPS & BOOK VALUE IMPACT
# =========================================================

elif menu == "EPS & Book Value Impact":

    st.header("📊 EPS & Book Value Per Share Impact of Equity Issuance")

    st.markdown("""
## Key Formulas

$$EPS_{after} = \\frac{\\text{Total Earnings After}}{\\text{Total Shares After}}$$

$$BVPS_{after} = \\frac{\\text{Total Equity After}}{\\text{Total Shares After}}$$

## Accretion vs Dilution Rule

| Condition | EPS Impact | Book Value Impact |
|---|---|---|
| New capital earnings > Ke × Proceeds | **EPS Accretive** | — |
| Issue price > Current BVPS | **BVPS Accretive** | — |
| Issue price < Current BVPS | **BVPS Dilutive** | — |
| Rights issue at any price | BVPS neutral (TERP equals) | — |
""")

    col1, col2 = st.columns(2)
    with col1:
        current_eps = st.number_input("Current EPS (₹)", value=20.0)
        current_bvps = st.number_input("Current BVPS (₹)", value=150.0)
        current_shares_m = st.number_input("Current Shares (Million)", value=100.0)
        net_income = st.number_input("Current Net Income (₹ Million)", value=2000.0)
    with col2:
        new_shares_m = st.number_input("New Shares to Issue (Million)", value=20.0)
        issue_p = st.number_input("Issue Price (₹)", value=140.0)
        roc_on_proceeds = st.number_input("Expected ROE on New Capital (%)", value=12.0)

    proceeds_m = new_shares_m * issue_p
    additional_earnings = proceeds_m * roc_on_proceeds / 100
    total_earnings = net_income + additional_earnings
    total_shares = current_shares_m + new_shares_m
    eps_new = total_earnings / total_shares

    total_equity_pre = current_bvps * current_shares_m
    total_equity_post = total_equity_pre + proceeds_m
    bvps_new = total_equity_post / total_shares

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Old EPS", f"₹{current_eps}")
    with col2:
        st.metric("New EPS", f"₹{round(eps_new,4)}")
    with col3:
        st.metric("Old BVPS", f"₹{current_bvps}")
    with col4:
        st.metric("New BVPS", f"₹{round(bvps_new,4)}")

    col1, col2 = st.columns(2)
    with col1:
        if eps_new > current_eps:
            st.success(f"✅ EPS ACCRETIVE (+₹{round(eps_new-current_eps,4)})")
        else:
            st.error(f"❌ EPS DILUTIVE (−₹{round(current_eps-eps_new,4)})")
    with col2:
        if bvps_new > current_bvps:
            st.success(f"✅ BVPS ACCRETIVE (+₹{round(bvps_new-current_bvps,4)})")
        elif bvps_new < current_bvps:
            st.warning(f"⚠️ BVPS DILUTIVE (−₹{round(current_bvps-bvps_new,4)})")
        else:
            st.info("BVPS NEUTRAL")

# =========================================================
# SEBI REGULATIONS
# =========================================================

elif menu == "SEBI Regulations":

    st.header("⚖️ SEBI Regulations for Equity Issuance")

    st.markdown("""
## Key SEBI Regulations
""")

    regs = pd.DataFrame({
        "Regulation": [
            "SEBI (ICDR) Regulations 2018",
            "Minimum Public Float",
            "IPO Eligibility",
            "Price Band",
            "Allotment Timeline",
            "Lock-in (Post IPO)",
            "Anchor Investors",
            "Greenshoe Option",
            "FPO Eligibility",
            "Rights Issue",
            "QIP Floor Price",
            "Insider Trading",
        ],
        "Key Provision": [
            "Issue of Capital and Disclosure Requirements — main framework for public issuances",
            "Minimum 25% public shareholding in listed companies",
            "3 years profitable track record OR promoter networth ≥ ₹100Cr OR agreement with QIB for 75%",
            "Max 20% band between floor and cap price",
            "Allotment within 6 working days of issue closure",
            "Promoters: 3 years (20% of post-IPO capital); others: 1 year",
            "Up to 60% of QIB portion to anchors; ≥10 anchor investors; min ₹10Cr each",
            "Over-allotment up to 15%; stabilisation agent buys from market within 30 days",
            "Listed for ≥1 year; no CBI/ED proceedings; minimum net worth ₹100Cr",
            "Notice period minimum 3 working days before record date",
            "Higher of 2-week average or 26-week WAP; max 5% discount",
            "SEBI (PIT) Regulations 2015 — trading window closure during sensitive periods",
        ]
    })

    st.table(regs)

    st.subheader("📋 SEBI IPO Eligibility Requirements (ICDR 2018)")

    st.info("""
**Track I (Main Board):** Tangible assets ≥ ₹3 Cr for 3 years;
Operating profit ≥ ₹15 Cr for 3 years; Net worth ≥ ₹1 Cr for 3 years.

**Track II (Profitability):** No profitability requirement but at least 75% of issue allocated to QIBs.
Minimum ₹100 Cr paid-up capital post-issue.

**SME IPO (SME Exchange):** Post-issue paid-up capital ≤ ₹25 Cr; simplified disclosures.

**Startup / New Economy IPOs:** DRHP must disclose key performance indicators (KPIs);
must disclose comparisons with listed global peers.
""")

# =========================================================
# COMPANIES ACT
# =========================================================

elif menu == "Companies Act 2013 — Equity Provisions":

    st.header("📖 Companies Act 2013 — Key Equity Provisions")

    provisions = pd.DataFrame({
        "Section": [
            "Section 23", "Section 24", "Section 42",
            "Section 43", "Section 54", "Section 55",
            "Section 62", "Section 63", "Section 68–70",
        ],
        "Topic": [
            "Public and Private Placement",
            "SEBI Oversight",
            "Private Placement",
            "Kinds of share capital",
            "Issue of sweat equity shares",
            "Issue of preference shares",
            "Further issue of share capital (Rights)",
            "Issue of bonus shares",
            "Buy-back of shares",
        ],
        "Key Requirement": [
            "Private: limited investors; Public: must comply with SEBI regulations",
            "SEBI has jurisdiction over listed company capital issuance",
            "Max 200 identified persons per FY; offer letter required; no advertising",
            "Equity shares (voting + residual claim) and preference shares (no voting usually)",
            "Can be issued to employees at discount or free; min 1-year employment",
            "Can be redeemable; must redeem from profits/new issue; can be irredeemable",
            "Existing shareholders must get first right; 15 days notice required",
            "Must be from free reserves/securities premium; not within 12 months of prior bonus",
            "Buy-back ≤ 25% of paid-up capital; board can approve ≤10%; 12-month gap required",
        ]
    })

    st.table(provisions)

# =========================================================
# EQUITY INSTRUMENT COMPARISON
# =========================================================

elif menu == "Equity Instrument Comparison":

    st.header("📊 Equity Instrument Comparison Dashboard")

    instruments = pd.DataFrame({
        "Method": ["IPO", "FPO", "Rights Issue", "Bonus Issue", "QIP", "Preferential",
                   "Private Placement", "ESOP", "VC", "PE", "ADR/GDR"],
        "Raises Cash": ["✅","✅","✅","❌","✅","✅","✅","Deferred","✅","✅","✅"],
        "Dilutes EPS": ["✅","✅","✅","✅","✅","✅","✅","✅ (exercise)","✅","✅","✅"],
        "SEBI Approval": ["Full","Full","Moderate","Nil","Simple","Moderate","Nil","Nil","Nil","Nil","SEC+SEBI"],
        "Speed": ["Slow (4-6m)","Slow","Moderate","Fast","Fast (1w)","Moderate","Fast","Fast","Fast","Fast","Very Slow"],
        "Investor Type": ["Public","Public","Existing","Existing","QIBs","Specific","Private","Employees","VC Funds","PE Funds","Foreign"],
        "Typical Discount": ["10-20%","5-10%","20-40%","N/A","3-5%","SEBI floor","Negotiated","Incentive price","Negotiated","Control premium","Negotiated"],
    })

    st.dataframe(instruments, use_container_width=True)

    st.subheader("🎯 Decision Guide: Which Method to Use?")

    q1 = st.radio("Is the company already listed?", ["Yes", "No"])

    if q1 == "No":
        q2 = st.radio("What stage is the company?",
                       ["Early startup", "Growth stage (profitable)", "Pre-IPO / Mature"])
        if q2 == "Early startup":
            st.success("**Recommended: Angel / Seed VC Funding** — Private placement to angel investors")
        elif q2 == "Growth stage (profitable)":
            st.success("**Recommended: Series A/B VC or PE** — Raise from institutional investors")
        else:
            st.success("**Recommended: IPO or Pre-IPO Private Placement + IPO** — Go public for exit liquidity")
    else:
        q3 = st.radio("What is the urgency?", ["Urgent (days)", "Moderate (weeks)", "Can wait (months)"])
        q4 = st.radio("Who should get shares?",
                       ["All investors", "Existing shareholders first", "Only institutions", "Specific investors"])
        if q3 == "Urgent (days)":
            st.success("**Recommended: QIP** — Fastest for listed companies; board approval only")
        elif q4 == "Existing shareholders first":
            st.success("**Recommended: Rights Issue** — Gives existing holders anti-dilution protection")
        elif q4 == "Only institutions":
            st.success("**Recommended: QIP or Preferential Allotment**")
        elif q4 == "Specific investors":
            st.success("**Recommended: Preferential Allotment** — For strategic investors, promoters")
        else:
            st.success("**Recommended: FPO** — Open to all investors; larger reach")

# =========================================================
# STEP-BY-STEP SOLVER
# =========================================================

elif menu == "Step-by-Step Solver":

    st.header("🧠 Step-by-Step Solver")

    problem = st.selectbox("Choose Problem", [
        "TERP (Rights Issue)",
        "Value of Right",
        "Cost of New Equity (Gordon)",
        "Post-issue EPS",
        "Ex-Bonus Price",
        "IPO Proceeds & Dilution",
    ])

    if problem == "TERP (Rights Issue)":
        cmp = st.number_input("CMP (₹)", value=500.0)
        ip = st.number_input("Issue Price (₹)", value=350.0)
        n = st.number_input("n (existing shares per right)", value=5.0)
        m = st.number_input("m (new shares per right)", value=1.0)

        st.write("**Step 1: TERP formula**")
        st.latex(r"TERP = \frac{n \times CMP + m \times Issue\ Price}{n + m}")
        terp = (n*cmp + m*ip)/(n+m)
        st.latex(f"TERP = \\frac{{{n}×{cmp} + {m}×{ip}}}{{{n}+{m}}} = {round(terp,4)}")
        st.success(f"TERP = ₹{round(terp,4)}")

    elif problem == "Value of Right":
        cmp = st.number_input("CMP (₹)", value=500.0, key="vor_c")
        ip = st.number_input("Issue Price (₹)", value=350.0, key="vor_ip")
        n = st.number_input("n", value=5.0, key="vor_n")
        m = st.number_input("m", value=1.0, key="vor_m")

        terp = (n*cmp + m*ip)/(n+m)
        val_right = cmp - terp
        st.write("**Step 1:** Compute TERP")
        st.latex(f"TERP = {round(terp,4)}")
        st.write("**Step 2:** Value of Right = CMP − TERP")
        st.success(f"Value of Right = {cmp} − {round(terp,4)} = ₹{round(val_right,4)}")

    elif problem == "Cost of New Equity (Gordon)":
        d0 = st.number_input("D₀ (₹)", value=5.0)
        p0 = st.number_input("P₀ (₹)", value=100.0)
        g = st.number_input("g (%)", value=8.0)
        f = st.number_input("Flotation f (%)", value=5.0)

        d1 = d0*(1+g/100)
        net_p = p0*(1-f/100)
        ke = d1/net_p*100 + g

        st.write("**Step 1:** D₁ = D₀(1+g)")
        st.latex(f"D_1 = {d0}(1+{g/100}) = {round(d1,4)}")
        st.write("**Step 2:** Net Proceeds = P₀(1−f)")
        st.latex(f"NP = {p0}(1-{f/100}) = {round(net_p,4)}")
        st.write("**Step 3:** Ke = D₁/NP + g")
        st.success(f"Ke = {round(d1,4)}/{round(net_p,4)} × 100 + {g} = {round(ke,4)}%")

    elif problem == "Post-issue EPS":
        old_eps = st.number_input("Current EPS (₹)", value=20.0)
        old_shares = st.number_input("Current Shares (Lakh)", value=100.0)
        new_shares = st.number_input("New Shares (Lakh)", value=20.0)
        add_earn = st.number_input("Additional Earnings from new capital (₹ Lakh)", value=80.0)

        total_earn = old_eps * old_shares * 100000 + add_earn * 100000
        total_sh = (old_shares + new_shares) * 100000
        new_eps = total_earn / total_sh

        st.write("**Step 1:** Total Earnings = Old + New")
        st.latex(f"Total = {old_eps}×{old_shares}L×100K + {add_earn}L×100K = {round(total_earn/100000,2)}L")
        st.write("**Step 2:** Total Shares = Old + New")
        st.latex(f"Shares = ({old_shares}+{new_shares}) × 1L = {old_shares+new_shares}L shares")
        st.success(f"New EPS = {round(total_earn/100000,2)}L / {old_shares+new_shares}L = ₹{round(new_eps,4)}")

    elif problem == "Ex-Bonus Price":
        cmp = st.number_input("Pre-bonus CMP (₹)", value=1000.0, key="eb_c")
        p = st.number_input("Bonus shares p (per q)", value=1.0, key="eb_p")
        q = st.number_input("Existing shares q", value=1.0, key="eb_q")

        ex_bonus = cmp*q/(p+q)
        st.write("**Step 1: Ex-bonus price formula**")
        st.latex(r"Ex\text{-}Bonus\ Price = \frac{CMP \times q}{p + q}")
        st.success(f"= {cmp}×{q}/({p}+{q}) = ₹{round(ex_bonus,4)}")

    elif problem == "IPO Proceeds & Dilution":
        fresh = st.number_input("Fresh Issue Shares (Lakh)", value=100.0)
        ofs = st.number_input("OFS Shares (Lakh)", value=50.0)
        price = st.number_input("Issue Price (₹)", value=500.0)
        pre_sh = st.number_input("Pre-IPO Shares (Lakh)", value=400.0)
        flot = st.number_input("Flotation Cost (%)", value=3.0)

        gross = (fresh+ofs)*100000*price
        to_company = fresh*100000*price*(1-flot/100)
        post = pre_sh + fresh
        dil = fresh/post*100

        st.write("**Step 1:** Gross proceeds = (Fresh+OFS) × Price")
        st.success(f"= {fresh+ofs}L × ₹{price} = {currency(gross)}")
        st.write("**Step 2:** Net to company = Fresh × Price × (1−flot)")
        st.success(f"= {fresh}L × {price} × {1-flot/100} = {currency(to_company)}")
        st.write("**Step 3:** Dilution = Fresh/(Pre+Fresh)")
        st.success(f"= {fresh}/({pre_sh}+{fresh}) = {round(dil,2)}%")

# =========================================================
# AI HINT SYSTEM
# =========================================================

elif menu == "AI Hint System":

    st.header("🤖 AI Hint System")

    problems_h = {
        "TERP Calculation": {
            "q": "A stock trades at ₹500. Rights issue: 1 new share for every 4 held at ₹300. Find TERP and value of right.",
            "correct": (4*500 + 1*300)/5,
            "hints": [
                "TERP = (n×CMP + m×Issue Price) / (n+m)",
                "n=4 (existing), m=1 (new), CMP=500, IP=300",
                "TERP = (4×500+1×300)/(4+1) = 2300/5",
            ],
            "formula": r"TERP = \frac{4\times500+1\times300}{5} = \frac{2300}{5} = 460"
        },
        "Cost of New Equity": {
            "q": "D₀=₹6, P₀=₹120, g=9%, Flotation cost=5%. Find cost of new equity.",
            "correct": 6*(1.09)/(120*0.95)*100 + 9,
            "hints": [
                "Ke = D₁/[P₀(1-f)] + g",
                "D₁ = D₀(1+g) = 6×1.09 = ₹6.54",
                "Net Proceeds = 120×(1-0.05) = ₹114"
            ],
            "formula": r"K_e = \frac{6 \times 1.09}{120 \times 0.95} + 9\% = \frac{6.54}{114} + 9\%"
        },
        "Ex-Bonus Price": {
            "q": "Company announces 1:2 bonus issue. CMP = ₹900. Find ex-bonus price.",
            "correct": 900*2/(1+2),
            "hints": [
                "Ex-bonus price = CMP × q / (p+q)",
                "Here p=1 (bonus), q=2 (existing)",
                "= 900 × 2/(1+2) = 1800/3"
            ],
            "formula": r"Ex\text{-}Bonus = \frac{900 \times 2}{1+2} = 600"
        }
    }

    sel = st.selectbox("Choose Problem", list(problems_h.keys()))
    prob = problems_h[sel]
    st.markdown(f"**Problem:** {prob['q']}")

    ans = st.number_input("Your Answer", value=0.0, key="re_hint_ans")
    if st.button("Check Answer"):
        correct = prob["correct"]
        if abs(ans - correct) < abs(correct)*0.02:
            st.success(f"✅ Correct! Answer = {round(correct,4)}")
            st.balloons()
        else:
            st.error(f"❌ Off. Use hints below.")

    for i, h in enumerate(prob["hints"], 1):
        if st.checkbox(f"Hint {i}", key=f"reh_{sel}_{i}"):
            st.info(f"💡 {h}")

    if st.checkbox("Show Solution", key=f"res_{sel}"):
        st.latex(prob["formula"])

# =========================================================
# QUIZ ENGINE
# =========================================================

elif menu == "Quiz Engine":

    st.header("📝 Raising Equity Quiz Engine")

    difficulty = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

    if "re_quiz_gen" not in st.session_state or st.button("🔄 New Question"):
        if difficulty == "Beginner":
            st.session_state.re_cmp = random.choice([400,500,600,800])
            st.session_state.re_ip = random.choice([250,300,350])
            st.session_state.re_n = random.choice([3,4,5])
            st.session_state.re_m = 1
            st.session_state.re_type = "terp"
        elif difficulty == "Intermediate":
            st.session_state.re_d0 = random.choice([4,5,6,8])
            st.session_state.re_p0 = random.choice([80,100,120,150])
            st.session_state.re_g = random.choice([7,8,9,10])
            st.session_state.re_f = random.choice([4,5,6])
            st.session_state.re_type = "ke_new"
        else:
            st.session_state.re_cmp_b = random.choice([600,800,1000,1200])
            st.session_state.re_pb = random.choice([1,2,3])
            st.session_state.re_qb = random.choice([1,2])
            st.session_state.re_type = "exbonus"
        st.session_state.re_quiz_gen = True

    qtype = st.session_state.re_type

    if qtype == "terp":
        cmp_q = st.session_state.re_cmp; ip_q = st.session_state.re_ip
        n_q = st.session_state.re_n; m_q = st.session_state.re_m
        correct = (n_q*cmp_q + m_q*ip_q)/(n_q+m_q)
        st.markdown(f"**Find TERP:**\n- CMP=₹{cmp_q}, Issue Price=₹{ip_q}, Ratio={m_q}:{n_q} (new:existing)")

    elif qtype == "ke_new":
        d0_q=st.session_state.re_d0; p0_q=st.session_state.re_p0
        g_q=st.session_state.re_g; f_q=st.session_state.re_f
        d1_q = d0_q*(1+g_q/100)
        correct = d1_q/(p0_q*(1-f_q/100))*100 + g_q
        st.markdown(f"**Find Cost of New Equity:**\n- D₀=₹{d0_q}, P₀=₹{p0_q}, g={g_q}%, Flotation={f_q}%")

    else:
        cmp_b=st.session_state.re_cmp_b; pb=st.session_state.re_pb; qb=st.session_state.re_qb
        correct = cmp_b*qb/(pb+qb)
        st.markdown(f"**Find Ex-Bonus Price:**\n- CMP=₹{cmp_b}, Bonus ratio={pb}:{qb} (new:existing)")

    ans = st.number_input("Your Answer (₹ or %)", value=0.0, key="re_quiz_ans")
    if st.button("Submit"):
        if abs(ans - correct) < max(0.5, abs(correct)*0.02):
            st.success(f"✅ Correct! = {round(correct,4)}")
            st.balloons()
        else:
            st.error(f"❌ Answer = {round(correct,4)}")

# =========================================================
# EXCEL FORMULA TRAINER
# =========================================================

elif menu == "Excel Formula Trainer":

    st.header("📊 Excel Formula Trainer")

    problems_ex = {
        "TERP": {
            "desc": "CMP=₹500, Rights ratio=1:4, Issue Price=₹300. Find TERP.",
            "fn": "=", "answer": "=(4*500+1*300)/(4+1)",
            "hint": "=(n*CMP + m*IssuePrice)/(n+m)"
        },
        "Value of Right": {
            "desc": "CMP=₹500, TERP=₹460. Find value of right.",
            "fn": "=", "answer": "=500-460",
            "hint": "=CMP - TERP"
        },
        "Ex-Bonus Price": {
            "desc": "CMP=₹900, Bonus 1:2. Find ex-bonus price.",
            "fn": "=", "answer": "=900*2/(1+2)",
            "hint": "=CMP*q/(p+q)"
        },
        "Cost of New Equity": {
            "desc": "D₀=₹5, P₀=₹100, g=8%, f=5%. Find Ke(new).",
            "fn": "=", "answer": "=(5*1.08/(100*0.95))+0.08",
            "hint": "=D1/(P0*(1-f)) + g  [all in decimal form]"
        },
        "Post-issue EPS": {
            "desc": "Old EPS=₹20, Old shares=100L, New shares=20L, New earnings=₹80L. Find new EPS.",
            "fn": "=",
            "answer": "=(20*100*100000+80*100000)/((100+20)*100000)",
            "hint": "=(Old_EPS*Old_Shares + New_Earnings)/(Old_Shares+New_Shares)"
        },
    }

    sel = st.selectbox("Choose Problem", list(problems_ex.keys()))
    prob = problems_ex[sel]
    st.subheader("Problem"); st.markdown(prob["desc"])
    st.info(f"💡 Hint: `{prob['hint']}`")

    user_inp = st.text_input("Enter Excel Formula")
    if st.button("Validate"):
        if user_inp.startswith("="):
            st.success(f"✅ Good approach! Reference: `{prob['answer']}`")
        else:
            st.error("Start with = for a formula")
    if st.checkbox("Show Answer"):
        st.code(prob["answer"], language="excel")

# =========================================================
# FORMULA CHEAT SHEET
# =========================================================

elif menu == "Formula Cheat Sheet":

    st.header("📘 Raising Equity — Formula Cheat Sheet")

    formulas = """
RAISING EQUITY — COMPLETE FORMULA REFERENCE
=============================================

──────────────────────────────────────────────────
RIGHTS ISSUE
──────────────────────────────────────────────────
1. Theoretical Ex-Rights Price (TERP)
   TERP = (n × CMP + m × Issue Price) / (n + m)
   n = existing shares per right; m = new shares per right

2. Value of 1 Right
   Value of Right = CMP − TERP
   Alt: = m × (CMP − Issue Price) / (n + m)

3. Rights Value to Investor
   Total value = Holdings × CMP = (Holdings + New shares) × TERP

──────────────────────────────────────────────────
BONUS ISSUE
──────────────────────────────────────────────────
4. Ex-Bonus Price
   Ex-Bonus Price = CMP × q / (p + q)
   p = bonus shares; q = existing shares

5. Adjusted EPS after Bonus
   Adjusted EPS = Old EPS × q / (p + q)

──────────────────────────────────────────────────
COST OF EQUITY
──────────────────────────────────────────────────
6. Cost of Retained Earnings (Gordon)
   Ke = D1/P0 + g = D0(1+g)/P0 + g

7. Cost of New Equity (with flotation)
   Ke(new) = D1/[P0(1-f)] + g
   f = flotation cost as % of issue price

8. Cost of Equity — CAPM
   Ke = Rf + β × (Rm − Rf)
   No flotation adjustment in CAPM approach

9. Cost of Equity — Bond Yield + RP
   Ke = Pre-tax Kd + Risk Premium (3-5%)

──────────────────────────────────────────────────
IPO / FPO CALCULATIONS
──────────────────────────────────────────────────
10. Net Proceeds to Company
    Net Proceeds = Fresh Shares × Issue Price × (1 − flotation%)

11. Public Float
    Public Float = Fresh Shares / Total Post-issue Shares

12. Dilution of Existing Owners
    Dilution = New Shares / Total Post-issue Shares

──────────────────────────────────────────────────
EPS & BOOK VALUE IMPACT
──────────────────────────────────────────────────
13. Post-issue EPS
    EPS(new) = (Total Earnings after) / (Total Shares after)
    EPS Accretive: if ROE on new capital > [D1/P0 + g]

14. Post-issue BVPS
    BVPS(new) = (Old Total Equity + New Proceeds) / Total Shares
    BVPS Accretive: if Issue Price > Old BVPS

──────────────────────────────────────────────────
VENTURE CAPITAL / PRIVATE EQUITY
──────────────────────────────────────────────────
15. Post-money Valuation
    Post-money = Pre-money + Investment

16. Investor Stake
    Investor % = Investment / Post-money

17. New Shares Issued (VC)
    New Shares = Pre-issue Shares × (Investment / Pre-money)

──────────────────────────────────────────────────
LBO RETURNS
──────────────────────────────────────────────────
18. MOIC (Multiple on Invested Capital)
    MOIC = Exit Equity Value / Entry Equity Invested

19. IRR from MOIC
    IRR = MOIC^(1/holding years) − 1

──────────────────────────────────────────────────
DEPOSITORY RECEIPTS
──────────────────────────────────────────────────
20. ADR Theoretical Price
    ADR Price (USD) = Indian Price (INR) / Exchange Rate × DR Ratio

──────────────────────────────────────────────────
QIP FLOOR PRICE
──────────────────────────────────────────────────
21. QIP Floor Price (SEBI)
    Floor = Max(2-week average, 26-week WAP)
    Max discount = 5% below floor price

──────────────────────────────────────────────────
KEY RULES TO REMEMBER
──────────────────────────────────────────────────
- TERP is ALWAYS between CMP and Issue Price
- Value of right = CMP - TERP (compensation for dilution)
- Bonus issue: No cash; share count rises; price falls proportionately
- Ke(new) > Ke(retained) always (due to flotation cost)
- EPS accretive: ROE on proceeds > current Ke
- BVPS accretive: Issue price > current BVPS
- IPO: Fresh issue (money to company) vs OFS (money to sellers)
- Rights issue: n:m ratio; n existing per m new
- QIP fastest equity raise for listed companies (3-7 days)
- Pecking order: Internal > Debt > Equity (new issue most costly)
=============================================
"""

    st.text_area("Formula Reference", formulas, height=800)
    st.download_button("📥 Download Formula Sheet", data=formulas,
                       file_name="Raising_Equity_Formulas.txt")

# =========================================================
# COMMON MISTAKES
# =========================================================

elif menu == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes in Raising Equity")

    mistakes = pd.DataFrame({
        "Mistake": [
            "Confusing TERP formula (n and m)",
            "Value of right = Issue Price - TERP (WRONG)",
            "Flotation cost not applied to Ke(new)",
            "Bonus issue raises cash (WRONG)",
            "Including OFS proceeds as company proceeds",
            "Rights issue always dilutes wealth (WRONG)",
            "CAPM Ke needs flotation adjustment",
            "EPS always falls after equity issue",
            "QIP available to all investors",
            "Adjusted EPS after bonus = Old EPS (WRONG)",
            "TERP equals CMP",
        ],
        "Correct Approach": [
            "TERP=(n×CMP + m×IP)/(n+m). n=existing shares per right; m=new shares.",
            "Value of right = CMP − TERP. (Not IP−TERP). Compensates for dilution.",
            "Ke(new) = D₁/[P₀(1−f)] + g. Net proceeds = P₀(1−f), not P₀.",
            "Bonus issue is a capitalisation — no cash changes hands. Reserves become paid-up capital.",
            "OFS proceeds go to selling shareholders, NOT the company. Only fresh issue proceeds go to company.",
            "If shareholder exercises rights: wealth unchanged (TERP compensates). Only lapsing rights loses value.",
            "CAPM Ke = Rf+β×ERP. No flotation adjustment needed for CAPM (market-based model).",
            "EPS can RISE (accretive) if returns on new capital > current Ke. EPS rises if earnings grow faster than shares.",
            "QIP is only for Qualified Institutional Buyers (QIBs). Not open to retail/public.",
            "After 1:1 bonus: EPS halves. After 1:2 bonus: EPS falls to 2/3. Adjust proportionately.",
            "TERP is always between CMP and Issue Price (since issue price < CMP for rights).",
        ]
    })

    st.table(mistakes)

    st.warning("""
**Top 5 Most Tested:**
1. TERP formula — n = existing, m = new; TERP = (n×CMP + m×IP)/(n+m)
2. Value of right = CMP - TERP (NOT IP - TERP)
3. Ke(new) uses net proceeds P₀(1-f), not P₀
4. Bonus issue → no cash raised; adjust EPS proportionately
5. OFS proceeds go to selling shareholders, not company
""")

# =========================================================
# ADVANCED QUIZ BANK
# =========================================================

elif menu == "Advanced Quiz Bank":

    st.header("📝 Advanced Quiz Bank — Raising Equity")

    level = st.selectbox("Difficulty", ["Beginner", "Intermediate", "Advanced"])

    if level == "Beginner":
        st.markdown("""
**Problem:** ABC Ltd. has 80 lakh shares at ₹600 each. It announces a rights issue of
1 new share for every 4 existing shares at ₹400.

(a) Calculate TERP
(b) Calculate value of one right
(c) New shares to be issued (lakh)
""")
        n_q=4; m_q=1; cmp_q=600; ip_q=400; pre_q=80
        terp_q=(n_q*cmp_q+m_q*ip_q)/(n_q+m_q)
        vor_q=cmp_q-terp_q
        new_q=pre_q*m_q/n_q

        c1,c2,c3=st.columns(3)
        c1.number_input("(a) TERP (₹)", value=0.0, step=0.01, key="aqb_beg_terp")
        c2.number_input("(b) Value of Right (₹)", value=0.0, step=0.01, key="aqb_beg_vor")
        c3.number_input("(c) New Shares (Lakh)", value=0.0, step=0.01, key="aqb_beg_ns")

        if st.button("Evaluate", key="beg_btn"):
            a1=st.session_state.aqb_beg_terp; a2=st.session_state.aqb_beg_vor; a3=st.session_state.aqb_beg_ns
            if all([abs(a1-terp_q)<0.5, abs(a2-vor_q)<0.5, abs(a3-new_q)<0.5]):
                st.success(f"✅ TERP={terp_q}, VoR={vor_q}, New Shares={new_q}L")
                st.balloons()
            else:
                st.error(f"TERP={terp_q} | VoR={vor_q} | New Shares={new_q}L")

    elif level == "Intermediate":
        st.markdown("""
**Problem:** XYZ Ltd. data: D₀=₹8, P₀=₹160, g=10%, Flotation cost=6%.
Also, for retained earnings use the same D₀, P₀, g.

(a) Cost of retained earnings  (b) Cost of new equity  (c) Difference (₹ extra cost of new equity)
""")
        d0_q=8; p0_q=160; g_q=10; f_q=6
        d1_q=d0_q*(1+g_q/100)
        ke_re_q=d1_q/p0_q*100+g_q
        ke_new_q=d1_q/(p0_q*(1-f_q/100))*100+g_q
        diff_q=ke_new_q-ke_re_q

        c1,c2,c3=st.columns(3)
        c1.number_input("(a) Ke(RE) %", value=0.0, step=0.01, key="aqb_int_ke_re")
        c2.number_input("(b) Ke(New) %", value=0.0, step=0.01, key="aqb_int_ke_new")
        c3.number_input("(c) Difference %", value=0.0, step=0.01, key="aqb_int_diff")

        if st.button("Evaluate", key="int_btn"):
            a1=st.session_state.aqb_int_ke_re; a2=st.session_state.aqb_int_ke_new; a3=st.session_state.aqb_int_diff
            if all([abs(a1-ke_re_q)<0.1, abs(a2-ke_new_q)<0.1, abs(a3-diff_q)<0.1]):
                st.success(f"✅ Ke(RE)={round(ke_re_q,4)}%, Ke(New)={round(ke_new_q,4)}%, Diff={round(diff_q,4)}%")
                st.balloons()
            else:
                st.error(f"Ke(RE)={round(ke_re_q,4)}% | Ke(New)={round(ke_new_q,4)}% | Diff={round(diff_q,4)}%")

    elif level == "Advanced":
        st.markdown("""
**Problem:** PQR Ltd. (listed) plans to raise ₹500 Cr via FPO.
- CMP = ₹800, FPO discount = 8%, Flotation cost = 2%
- Pre-FPO shares = 500 lakh, Pre-FPO EPS = ₹40
- Expected ROE on new capital = 15%

(a) FPO Issue Price
(b) New shares issued (lakh)
(c) Net proceeds to company (₹ Cr)
(d) Post-FPO EPS (accretive or dilutive?)
""")
        cmp_fpo=800; disc=8; flot=2; raise_cr=500
        pre_sh=500; old_eps=40; roe=15; tax_e=30

        ip_fpo=cmp_fpo*(1-disc/100)
        new_sh=raise_cr*1e7/(ip_fpo)/1e5  # in lakh
        net_proc=raise_cr*(1-flot/100)
        add_earn=net_proc*roe/100  # Cr
        total_earn=old_eps*pre_sh*1e5 + add_earn*1e7  # total in ₹
        post_sh=(pre_sh+new_sh)*1e5
        post_eps=total_earn/post_sh

        c1,c2,c3,c4=st.columns(4)
        c1.number_input("(a) Issue Price (₹)", value=0.0, step=0.01, key="aqb_adv_ip")
        c2.number_input("(b) New Shares (Lakh)", value=0.0, step=0.01, key="aqb_adv_ns")
        c3.number_input("(c) Net Proceeds (₹ Cr)", value=0.0, step=0.1, key="aqb_adv_np")
        c4.number_input("(d) Post-FPO EPS (₹)", value=0.0, step=0.01, key="aqb_adv_eps")

        if st.button("Evaluate", key="adv_btn"):
            a1=st.session_state.aqb_adv_ip; a2=st.session_state.aqb_adv_ns
            a3=st.session_state.aqb_adv_np; a4=st.session_state.aqb_adv_eps
            if all([abs(a1-ip_fpo)<0.5, abs(a2-new_sh)<0.1, abs(a3-net_proc)<1, abs(a4-post_eps)<0.1]):
                st.success(f"✅ IP=₹{round(ip_fpo,2)}, NS={round(new_sh,2)}L, NP=₹{round(net_proc,2)}Cr, EPS=₹{round(post_eps,4)}")
                st.balloons()
            else:
                st.error(f"IP=₹{round(ip_fpo,2)} | NS={round(new_sh,2)}L | NP=₹{round(net_proc,2)}Cr | EPS=₹{round(post_eps,4)}")

# =========================================================
# PROGRESS TRACKER
# =========================================================

elif menu == "Progress Tracker":

    st.header("📈 Student Progress Tracker")

    if "re_completed" not in st.session_state:
        st.session_state.re_completed = []
    if "re_scores" not in st.session_state:
        st.session_state.re_scores = []

    all_modules = [
        "Initial Public Offering (IPO)", "IPO Pricing & Book Building",
        "IPO Valuation Methods", "Follow-on Public Offer (FPO)",
        "Rights Issue", "Bonus Issue",
        "Private Placement", "Qualified Institutional Placement (QIP)",
        "Preferential Allotment", "Venture Capital (VC)", "Private Equity (PE)",
        "ESOP (Employee Stock Options)", "Convertible Instruments",
        "ADR & GDR", "Retained Earnings vs New Equity",
        "Cost of New Equity (Flotation Costs)", "Dilution Analysis",
        "EPS & Book Value Impact", "SEBI Regulations",
    ]

    selected = st.multiselect("Mark completed:", all_modules,
                              default=st.session_state.re_completed)
    st.session_state.re_completed = selected

    col1, col2 = st.columns(2)
    with col1:
        topic = st.selectbox("Quiz Topic", ["IPO/FPO", "Rights Issue", "Bonus Issue",
                                             "Private/QIP", "VC/PE", "Ke Calculations"])
    with col2:
        score = st.number_input("Score (%)", 0, 100, 75, key="re_score_inp")

    if st.button("Log Score"):
        st.session_state.re_scores.append({"topic": topic, "score": score})
        st.success("Score logged!")

    st.divider()
    n_done = len(selected); n_total = len(all_modules)
    st.metric("Modules Completed", f"{n_done}/{n_total}")
    st.progress(n_done / n_total)

    pub = sum(1 for m in selected if any(k in m for k in ["IPO","FPO","Rights","Bonus"]))
    priv = sum(1 for m in selected if any(k in m for k in ["Private","QIP","Preferential","VC","PE"]))
    instr = sum(1 for m in selected if any(k in m for k in ["ESOP","Convertible","ADR"]))
    analysis = sum(1 for m in selected if any(k in m for k in ["Retained","Cost","Dilution","EPS"]))

    col1,col2,col3,col4 = st.columns(4)
    col1.metric("Public Equity (5)", f"{pub}/5")
    col2.metric("Private Equity (5)", f"{priv}/5")
    col3.metric("Instruments (3)", f"{instr}/3")
    col4.metric("Analysis (4)", f"{analysis}/4")

    if st.session_state.re_scores:
        avg = sum(s["score"] for s in st.session_state.re_scores)/len(st.session_state.re_scores)
        st.metric("Average Score", f"{round(avg,1)}%")
        st.dataframe(pd.DataFrame(st.session_state.re_scores), use_container_width=True)

    if n_done == n_total:
        st.success("🏆 All Raising Equity modules complete!")
        st.balloons()

# =========================================================
# CASE-BASED LEARNING
# =========================================================

elif menu == "Case-Based Learning (Zomato IPO)":

    st.header("📚 Case Study: Zomato IPO (July 2021)")

    st.markdown("""
## Background

**Zomato Limited** — India's leading food delivery platform — conducted one of India's
most high-profile tech IPOs in July 2021.

---

## Key IPO Details

| Parameter | Detail |
|---|---|
| IPO Date | July 14–16, 2021 |
| Issue Size | ₹9,375 Crore |
| Fresh Issue | ₹9,000 Crore |
| OFS (Offer for Sale) | ₹375 Crore (Info Edge India) |
| Price Band | ₹72 – ₹76 per share |
| Issue Price | ₹76 (cap of band) |
| Listing Price | ₹116 (52.6% listing gain!) |
| Subscription | 38.25x overall; QIB: 51.8x; Retail: 7.5x |
| Lead Managers | Kotak, Morgan Stanley, BofA, Citibank |
| Valuation at IPO | ~₹64,365 Crore (approx. $8.6B) |
""")

    st.subheader("Step 1: IPO Proceeds Analysis")

    fresh = 9000; ofs = 375; price = 76; flotation = 2.5
    total_issue = fresh + ofs
    net_to_company = fresh * (1 - flotation/100)
    to_info_edge = ofs

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total IPO Size", f"₹{total_issue} Crore")
    with col2:
        st.metric("Net Proceeds to Zomato", f"₹{round(net_to_company,2)} Crore")
    with col3:
        st.metric("OFS Proceeds to Info Edge", f"₹{to_info_edge} Crore")

    st.subheader("Step 2: Subscription Analysis")

    fig = go.Figure(go.Bar(
        x=["Retail (RII)", "HNI (NII)", "QIB", "Overall"],
        y=[7.45, 33.54, 51.79, 38.25],
        marker_color=['#6B2137','#9B2C46','#C03B5E','#F5A623'],
        text=["7.45x","33.54x","51.79x","38.25x"], textposition='outside'
    ))
    fig.update_layout(title="Zomato IPO Subscription by Category",
                      yaxis_title="Times Subscribed")
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Step 3: Valuation at IPO")

    shares_post_ipo = 7600  # approximate in Crore rupees equivalent shares
    issue_price = 76
    st.markdown(f"""
- **Issue Price:** ₹76 per share
- **P/S Ratio at IPO:** ~25x (revenue-based since Zomato was loss-making)
- **EV/GMV:** ~5x Gross Merchandise Value
- Valuations based on **P/S, EV/GMV** (not P/E — negative earnings)
""")

    st.subheader("Step 4: Post-IPO Performance")

    dates = ["IPO Issue", "Listing Day", "6 Months", "1 Year", "2 Years"]
    prices_z = [76, 116, 68, 52, 90]

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=dates, y=prices_z, mode='lines+markers',
                              name='Zomato Share Price',
                              line=dict(color='#6B2137', width=2)))
    fig2.add_hline(y=76, line_dash="dash", line_color="gold",
                   annotation_text="Issue Price ₹76")
    fig2.update_layout(title="Zomato Post-IPO Price Journey",
                       yaxis_title="Share Price (₹)")
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Key Lessons from Zomato IPO")

    lessons = [
        "**New-age tech IPOs use alternate metrics** (P/S, EV/GMV) since profitability may be absent",
        "**OFS vs Fresh issue:** Info Edge monetised its early stake (OFS); company raised growth capital (Fresh)",
        "**Book building at cap:** 38x oversubscription → price set at ₹76 (cap of band)",
        "**Listing gain risk:** ₹116 on listing day → fell to ₹52 in 1 year → investing at IPO is not risk-free",
        "**SEBI new regulations post-Zomato:** New economy IPOs must disclose KPIs and global peer comparisons",
        "**Retail vs QIB behaviour:** QIBs bid 52x vs Retail 7.5x — institutional investors drove demand",
    ]
    for l in lessons:
        st.markdown(f"- {l}")

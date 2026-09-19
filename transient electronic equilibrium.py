import numpy as np
import matplotlib.pyplot as plt

# ============================================================
# 1. CHỈNH MÀU Ở ĐÂY
# ============================================================

COLOR_DOSE = "pink"       # Đường liều D
COLOR_KERMA = "skyblue"            # Đường K_col
COLOR_TEXT = "black"           # Chữ
COLOR_AXIS = "black"           # Trục
COLOR_ZMAX = "black"           # Đường z_max
COLOR_BUILDUP = "darkorange"   # Chữ Buildup region

# Ví dụ màu có thể dùng:
# "red", "blue", "green", "deeppink", "lightpink"
# "purple", "orange", "darkred", "navy", "teal"
# "#FF69B4"  --> màu hex


# ============================================================
# 2. FONT
# ============================================================

plt.rcParams["font.family"] = "Times New Roman"
plt.rcParams["mathtext.fontset"] = "stix"


# ============================================================
# 3. TẠO FIGURE
# ============================================================

fig, axes = plt.subplots(
    2, 1,
    figsize=(12, 10)
)


# ============================================================
# 4. HÀM VẼ MŨI TÊN TRỤC
# ============================================================

def arrow_axis(ax):
    ax.annotate(
        "",
        xy=(1.02, 0),
        xytext=(0, 0),
        xycoords="axes fraction",
        arrowprops=dict(
            arrowstyle="->",
            color=COLOR_AXIS,
            lw=1.5
        )
    )

    ax.annotate(
        "",
        xy=(0, 1.03),
        xytext=(0, 0),
        xycoords="axes fraction",
        arrowprops=dict(
            arrowstyle="->",
            color=COLOR_AXIS,
            lw=1.5
        )
    )


# ============================================================
# 5. (a) TRANSIENT ELECTRONIC EQUILIBRIUM
# ============================================================

ax = axes[0]

z = np.linspace(0, 10, 500)

# Đường dose D: tăng nhanh rồi tiến tới giá trị cân bằng
D1 = 1 - np.exp(-z / 1.25)

# Giới hạn D <= 1
D1 = np.minimum(D1, 1)

zmax = 2.5

# K_col
K1 = np.ones_like(z)

# ---- Đường dose ----
ax.plot(
    z,
    D1,
    color=COLOR_DOSE,
    lw=2.8,
    label=r"$D$ (dose)"
)

# ---- Đường K_col ----
ax.plot(
    z,
    K1,
    color=COLOR_KERMA,
    lw=2,
    ls="--",
    label=r"$K_{\mathrm{col}}$"
)

# ---- Đường zmax ----
ax.axvline(
    zmax,
    color=COLOR_ZMAX,
    lw=1.3,
    ls="--"
)

# ---- Dấu X tại zmax ----
ax.scatter(
    [zmax],
    [0.2],
    marker="x",
    s=150,
    color=COLOR_ZMAX,
    linewidths=2
)

# ---- Nhãn ----
ax.text(
    1.0, 0.68,
    r"$\beta < 1$",
    fontsize=16,
    color=COLOR_TEXT
)

ax.text(
    5.5, 0.90,
    r"$\beta = 1$",
    fontsize=16,
    color=COLOR_TEXT
)

ax.text(
    1.0, 0.48,
    r"$D$",
    fontsize=18,
    color=COLOR_DOSE
)

ax.text(
    1.1, 1.04,
    r"$K_{\mathrm{col}}$",
    fontsize=17,
    color=COLOR_KERMA
)

# ---- Buildup region ----
ax.text(
    1.25, 0.13,
    "Buildup\nregion",
    fontsize=15,
    ha="center",
    color=COLOR_BUILDUP
)

# ---- CPE ----
ax.text(
    6.1, 0.14,
    "CPE\n(Charged-particle equilibrium)",
    fontsize=15,
    ha="center",
    color=COLOR_TEXT
)

# ---- zmax ----
ax.text(
    zmax,
    -0.12,
    r"$z_{\max}$",
    fontsize=16,
    ha="center"
)

# ---- Mũi tên vùng ----
ax.annotate(
    "",
    xy=(9.5, 0.2),
    xytext=(0.3, 0.2),
    arrowprops=dict(
        arrowstyle="->",
        lw=1.3,
        color=COLOR_AXIS
    )
)

ax.annotate(
    "",
    xy=(0.3, 0.2),
    xytext=(1.8, 0.2),
    arrowprops=dict(
        arrowstyle="->",
        lw=1.3,
        color=COLOR_AXIS
    )
)

ax.set_title(
    r"(a) Transient electronic equilibrium ($\beta \leq 1$)",
    fontsize=19,
    fontweight="bold"
)

ax.set_ylabel(
    "Relative energy per unit mass",
    fontsize=15
)

ax.set_xlabel(
    "Depth in medium",
    fontsize=15
)

ax.set_xlim(0, 10)
ax.set_ylim(0, 1.15)

ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(
    fontsize=12,
    loc="upper right",
    frameon=True
)


# ============================================================
# 6. (b) TRANSIENT CPE / β > 1
# ============================================================

ax = axes[1]

z = np.linspace(0, 10, 500)

zmax = 2.5

# -----------------------------
# Dose D
# -----------------------------

# Phần buildup
D_buildup = 0.96 * (1 - np.exp(-z / 1.0))

# Sau zmax: giảm dần
D2 = np.where(
    z <= zmax,
    D_buildup,
    0.96 * np.exp(-(z - zmax) / 10)
)

# -----------------------------
# K_col
# -----------------------------

K2 = 1.08 - 0.062 * z


# ---- Dose ----
ax.plot(
    z,
    D2,
    color=COLOR_DOSE,
    lw=2.8,
    label=r"$D$ (dose)"
)

# ---- Kerma ----
ax.plot(
    z,
    K2,
    color=COLOR_KERMA,
    lw=2,
    ls=":",
    label=r"$K_{\mathrm{col}}$"
)

# ---- zmax ----
ax.axvline(
    zmax,
    color=COLOR_ZMAX,
    lw=1.3,
    ls="--"
)

# ---- Dấu X ----
ax.scatter(
    [zmax],
    [0.2],
    marker="x",
    s=150,
    color=COLOR_ZMAX,
    linewidths=2
)

# ---- β < 1 ----
ax.text(
    1.0, 0.65,
    r"$\beta < 1$",
    fontsize=16,
    color=COLOR_TEXT
)

# ---- β = 1 ----
ax.text(
    zmax - 0.1,
    1.02,
    r"$\beta = 1$",
    fontsize=16,
    color=COLOR_TEXT
)

# ---- β > 1 ----
ax.text(
    5.3, 0.85,
    r"$\beta > 1$",
    fontsize=16,
    color=COLOR_TEXT
)

# ---- D ----
ax.text(
    1.0, 0.47,
    r"$D$",
    fontsize=18,
    color=COLOR_DOSE
)

# ---- Kcol ----
ax.text(
    1.1, 1.06,
    r"$K_{\mathrm{col}}$",
    fontsize=17,
    color=COLOR_KERMA
)

# ---- Buildup ----
ax.text(
    1.25, 0.13,
    "Buildup\nregion",
    fontsize=15,
    ha="center",
    color=COLOR_BUILDUP
)

# ---- TCPE ----
ax.text(
    6.2, 0.14,
    "TCPE\n(Transient charged-particle equilibrium)",
    fontsize=15,
    ha="center",
    color=COLOR_TEXT
)

# ---- zmax ----
ax.text(
    zmax,
    -0.12,
    r"$z_{\max}$",
    fontsize=16,
    ha="center"
)

# ---- Mũi tên vùng ----
ax.annotate(
    "",
    xy=(9.5, 0.2),
    xytext=(0.3, 0.2),
    arrowprops=dict(
        arrowstyle="->",
        lw=1.3,
        color=COLOR_AXIS
    )
)

ax.annotate(
    "",
    xy=(0.3, 0.2),
    xytext=(1.8, 0.2),
    arrowprops=dict(
        arrowstyle="->",
        lw=1.3,
        color=COLOR_AXIS
    )
)

ax.set_title(
    r"(b) Loss of electronic equilibrium ($\beta > 1$)",
    fontsize=19,
    fontweight="bold"
)

ax.set_ylabel(
    "Relative energy per unit mass",
    fontsize=15
)

ax.set_xlabel(
    "Depth in medium",
    fontsize=15
)

ax.set_xlim(0, 10)
ax.set_ylim(0, 1.15)

ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1.0])

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.legend(
    fontsize=12,
    loc="upper right",
    frameon=True
)


# ============================================================
# 7. HIỂN THỊ
# ============================================================

plt.tight_layout()

plt.show()
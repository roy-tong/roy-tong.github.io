from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.units import mm
from pathlib import Path
import tempfile
import qrcode

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets/downloads/embodied-intelligence-preview-2026-summer.pdf'
BOOK_URL = 'https://roy-tong.github.io/book/'

pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
pdfmetrics.registerFont(TTFont('DejaVuSans', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))

W, H = A4
NAVY = HexColor('#0B2A3F')
CYAN = HexColor('#22B6C9')
TEAL = HexColor('#0F7E8F')
LIGHT = HexColor('#EAF5F7')
PALE = HexColor('#F4F8F9')
TEXT = HexColor('#173042')
MUTED = HexColor('#607480')
LINE = HexColor('#D7E4E8')
ORANGE = HexColor('#E88A12')
GREEN = HexColor('#1D7A65')
M = 18 * mm
CONTENT_W = W - 2 * M

with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp:
    QR = Path(tmp.name)
qr = qrcode.QRCode(version=4, box_size=12, border=3)
qr.add_data(BOOK_URL)
qr.make(fit=True)
qr.make_image(fill_color='black', back_color='white').save(QR)

OUT.parent.mkdir(parents=True, exist_ok=True)
c = canvas.Canvas(str(OUT), pagesize=A4)
c.setTitle('《具身智能入门》试读版（2026 夏季版）')
c.setAuthor('Roy Tong（仝夏瑞）')
c.setSubject('具身智能产业、公司、产品、技术与职业地图免费试读版')
c.setKeywords('具身智能, 人形机器人, VLA, 世界模型, 产品经理, 求职')


def cn_width(text, font, size):
    return stringWidth(text, font, size)


def split_cn(text, font='STSong-Light', size=10.5, max_width=CONTENT_W):
    lines = []
    for para in text.split('\n'):
        if not para:
            lines.append('')
            continue
        cur = ''
        for ch in para:
            if cn_width(cur + ch, font, size) <= max_width:
                cur += ch
            else:
                lines.append(cur)
                cur = ch
        if cur:
            lines.append(cur)
    return lines


def draw_text(text, x, y, font='STSong-Light', size=10.5, color=TEXT, leading=16, max_width=None):
    if max_width is None:
        max_width = CONTENT_W
    c.setFillColor(color)
    c.setFont(font, size)
    for line in split_cn(text, font, size, max_width):
        c.drawString(x, y, line)
        y -= leading
    return y


def draw_bullets(items, x, y, width, size=10, leading=15, bullet_color=CYAN, gap=7):
    for item in items:
        c.setFillColor(bullet_color)
        c.circle(x + 3, y - 4, 2.2, fill=1, stroke=0)
        y = draw_text(item, x + 13, y, size=size, leading=leading, max_width=width - 13)
        y -= gap
    return y


def header(section, title, page_no, subtitle=None):
    c.setFillColor(PALE)
    c.rect(0, 0, W, H, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.rect(0, H - 22 * mm, W, 22 * mm, fill=1, stroke=0)
    c.setFillColor(CYAN)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawString(M, H - 11.5 * mm, section.upper())
    c.setFillColor(white)
    c.setFont('STSong-Light', 18)
    c.drawString(M, H - 18 * mm, title)
    if subtitle:
        c.setFillColor(MUTED)
        c.setFont('STSong-Light', 9.5)
        c.drawString(M, H - 29 * mm, subtitle)
    c.setStrokeColor(LINE)
    c.line(M, 13 * mm, W - M, 13 * mm)
    c.setFillColor(MUTED)
    c.setFont('STSong-Light', 7.5)
    c.drawString(M, 8 * mm, '《具身智能入门》免费试读版 | 2026 夏季版')
    c.drawRightString(W - M, 8 * mm, f'{page_no} / 12')


def card(x, y, w, h, title, body=None, accent=CYAN, title_size=12):
    c.setFillColor(white)
    c.roundRect(x, y - h, w, h, 6, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, y - h, w, h, 6, fill=0, stroke=1)
    c.setFillColor(accent)
    c.rect(x, y - h, w, 3, fill=1, stroke=0)
    c.setFillColor(TEXT)
    c.setFont('STSong-Light', title_size)
    c.drawString(x + 12, y - 22, title)
    if body:
        draw_text(body, x + 12, y - 42, size=9.2, color=MUTED, leading=14, max_width=w - 24)


# 1 Cover
c.setFillColor(NAVY)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setStrokeColor(Color(0.2, 0.65, 0.72, alpha=0.12))
c.setLineWidth(0.5)
for x in range(0, int(W), 36):
    c.line(x, 0, x, H)
for y in range(0, int(H), 36):
    c.line(0, y, W, y)
cx, cy = W - 125, H - 185
for r in (38, 72, 106):
    c.circle(cx, cy, r, stroke=1, fill=0)
c.setFillColor(CYAN)
c.circle(cx, cy, 7, fill=1, stroke=0)
for px, py in [(cx, cy + 106), (cx - 72, cy), (cx + 106, cy + 15)]:
    c.circle(px, py, 5, fill=1, stroke=0)
c.setFillColor(CYAN)
c.setFont('DejaVuSans-Bold', 8)
c.drawString(M, H - 47 * mm, 'PHYSICAL AI / FREE READER PREVIEW')
c.setFillColor(TEAL)
c.roundRect(M, H - 68 * mm, 58 * mm, 9 * mm, 0, fill=1, stroke=0)
c.setFillColor(white)
c.setFont('STSong-Light', 9)
c.drawCentredString(M + 29 * mm, H - 64.5 * mm, '免费精华试读版 · 可完整转发')
c.setFillColor(white)
c.setFont('STSong-Light', 31)
c.drawString(M, H - 100 * mm, '《具身智能入门》')
c.setFont('STSong-Light', 23)
c.drawString(M, H - 116 * mm, '试读版')
c.setStrokeColor(CYAN)
c.setLineWidth(2.2)
c.line(M, H - 128 * mm, M + 72 * mm, H - 128 * mm)
c.setFillColor(HexColor('#C9DDE6'))
c.setFont('STSong-Light', 13)
c.drawString(M, H - 143 * mm, '产业、公司、产品、技术与职业地图')
c.setFillColor(HexColor('#8FB0BE'))
c.setFont('STSong-Light', 9.5)
c.drawString(M, H - 158 * mm, '12 页精华内容 · 约 15 分钟读完 · 先判断是否值得购买完整版')
c.setFillColor(white)
c.setFont('STSong-Light', 10)
c.drawString(M, 59 * mm, '作者  Roy Tong（仝夏瑞）')
c.setFillColor(HexColor('#93B7C4'))
c.setFont('DejaVuSans', 8.5)
c.drawString(M, 51 * mm, 'roy-tong.github.io/book/')
c.setFont('STSong-Light', 8.5)
c.drawString(M, 42 * mm, '2026 夏季版  |  数据截止 2026-07-20')
c.showPage()

# 2 Why
header('01 / WHY THIS GUIDE', '为什么具身智能越学越乱', 2, '不是资料不够，而是产品、技术、公司和资本被放在了同一层级')
y = H - 40 * mm
y = draw_text('一个刚进入具身智能的人，往往会同时遇到人形机器人、四足机器人、VLA、世界模型、数据采集、融资新闻和招聘信息。每条信息都像是关键，但它们回答的是不同问题。', M, y, size=11.2, leading=18)
y -= 10
card(M, y, CONTENT_W, 57 * mm, '这本书先回答五个问题', accent=CYAN)
y -= 13 * mm
y = draw_bullets([
    '具身智能的边界在哪里，人形在整个机器人产业中处于什么位置？',
    '不同类型的公司应该如何分类，哪些数据才能支撑比较？',
    '产品为什么采用人形、四足、轮式双臂或固定机械臂？',
    '本体、控制、VLA、世界模型、数据和触觉怎样组成完整系统？',
    '如果想加入这个行业，应该选择什么公司、岗位和学习路线？'
], M + 12, y, CONTENT_W - 24, size=10.2, leading=15, gap=5)
y -= 8
c.setFillColor(LIGHT)
c.roundRect(M, y - 30 * mm, CONTENT_W, 30 * mm, 5, fill=1, stroke=0)
c.setFillColor(TEAL)
c.setFont('STSong-Light', 13)
c.drawString(M + 12, y - 13 * mm, '试读版的目标不是把内容讲完')
draw_text('而是让你判断：这套“先建地图、再研究公司和技术”的方法，是否能减少你的信息焦虑和重复学习。', M + 12, y - 22 * mm, size=10, color=TEXT, leading=15, max_width=CONTENT_W - 24)
c.showPage()

# 3 Framework
header('02 / THE MAP', '一张图看懂全书框架', 3, '从行业与场景出发，最终落到岗位与个人选择')
y = H - 41 * mm
cols = [
    ('产业地图', '边界、八层产业链、产品形态、B/C 端场景、商业化与资本', '知道一条信息应该放在哪个层级'),
    ('公司研究', '国内外工业、物流、服务、消费、医疗、足式、人形、模型、数据和部件公司', '在同品类、同任务、同阶段中比较公司'),
    ('产品与技术', '本体、感知、控制、VLA、世界模型、数据、仿真、触觉、安全与部署', '从客户任务倒推产品形态和技术选择'),
    ('职业与学习', '岗位地图、招聘、薪酬、员工体验、公司选择与学习计划', '把行业知识转成求职判断与作品')
]
box_h = 38 * mm
for i, (title, body, result) in enumerate(cols):
    yy = y - i * (box_h + 7)
    c.setFillColor(white)
    c.roundRect(M, yy - box_h, CONTENT_W, box_h, 6, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(M, yy - box_h, CONTENT_W, box_h, 6, fill=0, stroke=1)
    c.setFillColor(CYAN)
    c.roundRect(M + 8, yy - 28, 34, 18, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawCentredString(M + 25, yy - 22, f'{i + 1:02d}')
    c.setFillColor(TEXT)
    c.setFont('STSong-Light', 13)
    c.drawString(M + 51, yy - 22, title)
    draw_text(body, M + 51, yy - 42, size=9.2, color=MUTED, leading=13, max_width=CONTENT_W - 63)
    c.setFillColor(LIGHT)
    c.roundRect(W - M - 165, yy - box_h + 9, 153, 23, 4, fill=1, stroke=0)
    draw_text(result, W - M - 157, yy - box_h + 24, size=8.3, color=TEAL, leading=11, max_width=139)
c.setFillColor(NAVY)
c.roundRect(M, 36 * mm, CONTENT_W, 18 * mm, 5, fill=1, stroke=0)
c.setFillColor(white)
c.setFont('STSong-Light', 11)
c.drawCentredString(W / 2, 43 * mm, '行业与场景  →  公司与商业  →  产品与技术  →  岗位与个人选择')
c.showPage()

# 4 Scale
header('03 / SCALE', '先建立量级感：六个关键数字', 4, '不同品类口径不能直接相加；这些数字只用来建立行业坐标')
items = [
    ('54.2 万台', '全球工业机器人 2024 年新安装', '成熟制造、集成和服务体系已经形成'),
    ('1.3–1.8 万台', '全球人形机器人 2025 年公开统计', '关注度高，但当期出货仍处早期'),
    ('16.99 亿元', '宇树科技 2025 年收入', '提供可审计的经营规模样本'),
    ('12 万台+', '普渡机器人累计出货', '成熟非人形服务机器人是商业化基准'),
    ('200 家+', 'WAIC 2026 具身产业链企业', '说明产业参与度，不等于商业成熟度'),
    ('100 个+', '高价值应用场景政策目标', '是验证与部署目标，不是已完成销量')
]
card_w = (CONTENT_W - 10) / 2
card_h = 48 * mm
start_y = H - 43 * mm
for i, (num, label, meaning) in enumerate(items):
    col = i % 2
    row = i // 2
    x = M + col * (card_w + 10)
    y = start_y - row * (card_h + 10)
    c.setFillColor(white)
    c.roundRect(x, y - card_h, card_w, card_h, 6, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, y - card_h, card_w, card_h, 6, fill=0, stroke=1)
    c.setFillColor(TEAL if i < 4 else ORANGE)
    c.setFont('DejaVuSans-Bold', 20)
    c.drawString(x + 12, y - 25, num)
    draw_text(label, x + 12, y - 45, size=9.5, color=TEXT, leading=14, max_width=card_w - 24)
    draw_text(meaning, x + 12, y - card_h + 25, size=8.4, color=MUTED, leading=12, max_width=card_w - 24)
c.setFillColor(LIGHT)
c.roundRect(M, 25 * mm, CONTENT_W, 23 * mm, 5, fill=1, stroke=0)
draw_text('核心判断：具身智能已经是大产业，但通用人形仍是小市场。下一阶段的分化，要由任务验收、复购和部署经济性决定。', M + 12, 39 * mm, size=10, color=TEXT, leading=14, max_width=CONTENT_W - 24)
c.showPage()

# 5 Six judgments
header('04 / SIX JUDGMENTS', '六个行业判断', 5, '用来过滤融资新闻、演示视频和热门概念')
judgments = [
    ('人形是重要试验场，但不是整个产业', '工业、物流、服务、消费、医疗和四足机器人都有独立的客户、任务和商业链条。'),
    ('行业正从“动作演示”转向“任务化工作单元”', '进入客户现场后，评价标准会变成完整任务成功率、节拍、接管率、连续运行和单位任务成本。'),
    ('产能、下线、出货、交付、验收、收入和复购不是同一件事', '研究公司时必须把每个数字放回制造、部署、客户确认和会计结果的节点。'),
    ('VLA、世界模型和数据基础设施共同构成平台竞争', '通用能力不仅取决于模型大小，也取决于失败数据、跨本体迁移和长程恢复。'),
    ('成熟公司和前沿公司应该放在不同坐标中', '成熟公司提供客户、制造、质量和财务基准；前沿公司探索新本体、模型、数据和产品入口。'),
    ('求职时，公司热度不能替代岗位事实', '岗位价值取决于团队目标、管理者、资源与权限、交付物和可迁移能力。')
]
y = H - 42 * mm
for i, (title, body) in enumerate(judgments):
    c.setFillColor(CYAN)
    c.circle(M + 9, y - 5, 9, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawCentredString(M + 9, y - 8, str(i + 1))
    c.setFillColor(TEXT)
    c.setFont('STSong-Light', 11.2)
    c.drawString(M + 29, y, title)
    y = draw_text(body, M + 29, y - 18, size=9.2, color=MUTED, leading=13, max_width=CONTENT_W - 29)
    y -= 13
c.showPage()

# 6 Company research
header('05 / COMPANY RESEARCH', '怎样研究一家公司', 6, '不按媒体声量、融资额或作者熟悉程度挑选公司')
rows = [
    ('业务定义', '客户、付费者、任务、产品形态与收入方式', '公司靠什么创造客户价值？'),
    ('经营证据', '收入、利润/亏损、销量/装机、客户数、任务量与复购', '已经发生的业务达到什么数量级？'),
    ('产品能力', '环境、对象、完整工作流、成功率、节拍、接管和故障', '产品在真实环境中稳定完成什么任务？'),
    ('技术路线', '构型、执行器、感知、控制、VLA/世界模型、数据与部署', '哪项技术选择改变了任务结果或成本？'),
    ('交付经济性', 'POC 时间、部署人天、定制比例、运维、SLA 与回本期', '交付越多，是否变得更容易和更便宜？'),
    ('资本与组织', '融资交割、估值口径、现金用途、股东、上市状态与招聘', '公司正在用资源购买哪一个里程碑？')
]
x0 = M
y0 = H - 42 * mm
colw = [34 * mm, 78 * mm, CONTENT_W - 112 * mm]
rh = 24 * mm
c.setFillColor(NAVY)
c.roundRect(x0, y0 - 12 * mm, CONTENT_W, 12 * mm, 4, fill=1, stroke=0)
for j, (head, width) in enumerate(zip(['维度', '需要查找的信息', '最终要回答的问题'], colw)):
    c.setFillColor(white)
    c.setFont('STSong-Light', 9.5)
    c.drawString(x0 + sum(colw[:j]) + 7, y0 - 8 * mm, head)
y = y0 - 12 * mm
for i, row in enumerate(rows):
    c.setFillColor(white if i % 2 == 0 else PALE)
    c.rect(x0, y - rh, CONTENT_W, rh, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(x0, y - rh, x0 + CONTENT_W, y - rh)
    for j, text in enumerate(row):
        draw_text(text, x0 + sum(colw[:j]) + 7, y - 9 * mm, size=8.5 if j else 9.4, color=TEXT if j != 1 else MUTED, leading=11, max_width=colw[j] - 12)
    y -= rh
c.setFillColor(LIGHT)
c.roundRect(M, 22 * mm, CONTENT_W, 28 * mm, 5, fill=1, stroke=0)
draw_text('一张合格的公司卡至少保留：3 条已确认事实、3 个关键未知、2 个持续跟踪数据、1 个让当前判断失效的条件。', M + 12, 39 * mm, size=10, color=TEXT, leading=14, max_width=CONTENT_W - 24)
c.showPage()

# 7 Evidence chain
header('06 / EVIDENCE CHAIN', '别把“产能、交付和收入”混成一个数字', 7, '公司商业化研究需要把证据放回它所在的节点')
stages = [('产能', '理论制造上限'), ('下线', '完成生产'), ('出货', '离开工厂'), ('交付', '进入客户现场'), ('验收', '客户确认结果'), ('收入', '会计确认'), ('复购', '重复购买')]
y = H - 56 * mm
gap = 7
sw = (CONTENT_W - gap * 6) / 7
for i, (stage, detail) in enumerate(stages):
    x = M + i * (sw + gap)
    c.setFillColor(CYAN if i < 4 else GREEN)
    c.roundRect(x, y - 23 * mm, sw, 23 * mm, 5, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('STSong-Light', 11)
    c.drawCentredString(x + sw / 2, y - 8 * mm, stage)
    c.setFont('STSong-Light', 7.4)
    c.drawCentredString(x + sw / 2, y - 17 * mm, detail)
    if i < 6:
        c.setStrokeColor(MUTED)
        c.line(x + sw + 1, y - 11.5 * mm, x + sw + gap - 1, y - 11.5 * mm)
        c.line(x + sw + gap - 4, y - 14 * mm, x + sw + gap - 1, y - 11.5 * mm)
        c.line(x + sw + gap - 4, y - 9 * mm, x + sw + gap - 1, y - 11.5 * mm)
y -= 40 * mm
c.setFillColor(TEXT)
c.setFont('STSong-Light', 14)
c.drawString(M, y, '四类常见误读')
y -= 17
misreads = [
    ('“规划年产 1 万台”', '说明制造规划，不等于已卖出 1 万台。'),
    ('“与客户达成合作”', '可能只是框架协议、POC 或渠道合作。'),
    ('“进入某工厂试点”', '需要继续确认任务、台数、节拍、接管和验收。'),
    ('“获得大额融资”', '说明获得资源，不自动证明产品已经形成复购。')
]
for i, (title, body) in enumerate(misreads):
    x = M + (i % 2) * (card_w + 10)
    yy = y - (i // 2) * 42 * mm
    c.setFillColor(white)
    c.roundRect(x, yy - 34 * mm, card_w, 34 * mm, 5, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, yy - 34 * mm, card_w, 34 * mm, 5, fill=0, stroke=1)
    c.setFillColor(ORANGE)
    c.setFont('STSong-Light', 10.5)
    c.drawString(x + 12, yy - 15, title)
    draw_text(body, x + 12, yy - 34, size=8.8, color=MUTED, leading=13, max_width=card_w - 24)
c.setFillColor(NAVY)
c.roundRect(M, 25 * mm, CONTENT_W, 20 * mm, 5, fill=1, stroke=0)
c.setFillColor(white)
c.setFont('STSong-Light', 10)
c.drawCentredString(W / 2, 33 * mm, '真正值得追踪的是：完整任务 → 验收 → 规模交付 → 收入 → 复购')
c.showPage()

# 8 Product and technology
header('07 / PRODUCT & TECHNOLOGY', '从任务出发，理解机器人系统', 8, '客户与场景 → 任务与验收 → 产品形态 → 系统架构 → 技术取舍 → 部署经济性')
nodes = [
    ('本体与执行', '能否进入目标空间并完成移动、抓取、操作和接触？'),
    ('感知与状态', '如何理解环境、物体、人、自身状态和接触变化？'),
    ('规划与控制', '高层任务、运动规划、力控和实时安全怎样分工？'),
    ('VLA 与世界模型', '用于语义理解、动作生成、后果预测还是长程规划？'),
    ('数据与训练', '真机、遥操、视频、仿真和合成数据如何配合？'),
    ('评测与安全', '成功率、节拍、接管、P95 时长、MTBF 和失败后果如何定义？'),
    ('部署与运营', '安装、标定、示教、OTA、维修、远程运营和 SLA 需要多少资源？')
]
y = H - 42 * mm
for i, (title, body) in enumerate(nodes):
    x = M if i % 2 == 0 else M + card_w + 10
    row = i // 2
    yy = y - row * 46 * mm
    width = CONTENT_W if i == 6 else card_w
    if i == 6:
        x = M
    c.setFillColor(white)
    c.roundRect(x, yy - 37 * mm, width, 37 * mm, 5, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(x, yy - 37 * mm, width, 37 * mm, 5, fill=0, stroke=1)
    c.setFillColor(TEAL)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawString(x + 11, yy - 14, f'{i + 1:02d}')
    c.setFillColor(TEXT)
    c.setFont('STSong-Light', 10.5)
    c.drawString(x + 34, yy - 14, title)
    draw_text(body, x + 11, yy - 31, size=8.5, color=MUTED, leading=12, max_width=width - 22)
c.setFillColor(LIGHT)
c.roundRect(M, 22 * mm, CONTENT_W, 28 * mm, 5, fill=1, stroke=0)
draw_text('判断一项技术是否重要，追问三件事：改善了哪个完整任务指标？在什么条件下成立？增益能否覆盖算力、数据、硬件、延迟和维护成本？', M + 12, 39 * mm, size=9.7, color=TEXT, leading=14, max_width=CONTENT_W - 24)
c.showPage()

# 9 Career
header('08 / CAREER', '怎样用于求职与学习', 9, '公司选择和岗位选择必须分开')
roles = ['模型 / 算法', '运动控制', '机器人软件', '机械结构', '电气 / 嵌入式', '数据 / 评测', '产品 / 项目', '行业方案 / 销售', '交付 / 售后', '供应链 / 制造', '职能管理']
c.setFillColor(TEXT)
c.setFont('STSong-Light', 12)
c.drawString(M, H - 42 * mm, '具身智能不是只有算法工程师')
rx = M
ry = H - 52 * mm
for i, role in enumerate(roles):
    width = max(56, cn_width(role, 'STSong-Light', 9) + 20)
    if rx + width > W - M:
        rx = M
        ry -= 28
    c.setFillColor(LIGHT if i % 2 == 0 else white)
    c.roundRect(rx, ry - 18, width, 18, 9, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(rx, ry - 18, width, 18, 9, fill=0, stroke=1)
    c.setFillColor(TEAL)
    c.setFont('STSong-Light', 9)
    c.drawCentredString(rx + width / 2, ry - 13, role)
    rx += width + 7

y = H - 82 * mm
cw = (CONTENT_W - 12) / 2
c.setFillColor(NAVY)
c.roundRect(M, y - 11 * mm, cw, 11 * mm, 4, fill=1, stroke=0)
c.roundRect(M + cw + 12, y - 11 * mm, cw, 11 * mm, 4, fill=1, stroke=0)
c.setFillColor(white)
c.setFont('STSong-Light', 11)
c.drawCentredString(M + cw / 2, y - 7 * mm, '公司层面')
c.drawCentredString(M + cw + 12 + cw / 2, y - 7 * mm, '岗位层面')
left = ['公司属于哪一品类，靠什么业务生存？', '产品进入演示、POC、交付还是复购？', '现金、收入和融资能支撑多长时间？', '组织是在扩张、调整方向还是完成短期项目？', '是在建立可复用产品，还是持续消耗人力定制？']
right = ['岗位是新增、替补还是长期人才池？', '入职后 90 天和半年的核心交付物是什么？', '真机、数据、算力、客户和交付资源如何分配？', '直接管理者、决策方式和绩效标准怎样？', '即使公司不及预期，个人能留下什么能力资产？']
y -= 18 * mm
for i in range(5):
    height = 28 * mm
    for col, values in enumerate([left, right]):
        x = M + col * (cw + 12)
        c.setFillColor(white if i % 2 == 0 else PALE)
        c.rect(x, y - height, cw, height, fill=1, stroke=0)
        c.setStrokeColor(LINE)
        c.rect(x, y - height, cw, height, fill=0, stroke=1)
        draw_text(values[i], x + 10, y - 11 * mm, size=8.7, color=TEXT, leading=12, max_width=cw - 20)
    y -= height
c.showPage()

# 10 How to read
header('09 / HOW TO READ', '三种读法：把阅读变成可交付结果', 10, '完整版不是名词汇编，而是一套可以反复使用的研究工具')
paths = [
    ('第一次系统学习', '按顺序阅读产业、公司、产品技术与职业章节', '能用一张图解释产业链、产品形态、场景和技术系统'),
    ('正在研究公司或市场', '重点阅读公司研究、商业化、资本和产品技术章节', '完成一家公司的经营、产品、技术、资本与风险卡'),
    ('准备转行或求职', '先看公司池、岗位地图和求职研究，再回看目标品类', '形成目标公司清单、求职公司卡和面试核验问题')
]
y = H - 43 * mm
for who, path, outcome in paths:
    height = 48 * mm
    c.setFillColor(white)
    c.roundRect(M, y - height, CONTENT_W, height, 6, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.roundRect(M, y - height, CONTENT_W, height, 6, fill=0, stroke=1)
    c.setFillColor(CYAN)
    c.roundRect(M + 12, y - 29, 74, 20, 4, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont('STSong-Light', 9.3)
    c.drawCentredString(M + 49, y - 23, who)
    c.setFillColor(TEXT)
    c.setFont('STSong-Light', 10.2)
    c.drawString(M + 100, y - 19, '建议路径')
    draw_text(path, M + 100, y - 36, size=9, color=MUTED, leading=13, max_width=CONTENT_W - 112)
    c.setFillColor(LIGHT)
    c.roundRect(M + 12, y - height + 10, CONTENT_W - 24, 18, 4, fill=1, stroke=0)
    c.setFillColor(TEAL)
    c.setFont('STSong-Light', 8.8)
    c.drawString(M + 21, y - height + 16, '阅读后的交付物：' + outcome)
    y -= height + 10
c.showPage()

# 11 Full edition comparison
header('10 / FULL EDITION', '免费试读版与 120 页正式版的区别', 11, '先确认框架和写作方式，再决定是否购买')
rows = [
    ('篇幅', '12 页精华试读', '120 页 PDF'),
    ('用途', '判断框架和写作方式是否适合自己', '系统建立行业、公司、产品、技术和职业地图'),
    ('公司研究', '展示分析框架', '80 余家公司分类 + 39 家首轮跟踪矩阵'),
    ('产品技术', '展示系统节点', '展开本体、控制、模型、数据、仿真、触觉、评测与部署'),
    ('职业部分', '展示公司/岗位判断', '岗位族、招聘、薪酬、员工体验和学习路线'),
    ('研究工具', '无完整模板', '公司工作表、数据字典、术语速查和主要资料索引')
]
x = M
y = H - 44 * mm
widths = [36 * mm, 62 * mm, CONTENT_W - 98 * mm]
rh = 27 * mm
c.setFillColor(NAVY)
c.roundRect(x, y - 12 * mm, CONTENT_W, 12 * mm, 4, fill=1, stroke=0)
for j, title in enumerate(['对比项', '试读版', '正式版']):
    c.setFillColor(white)
    c.setFont('STSong-Light', 9.5)
    c.drawString(x + sum(widths[:j]) + 8, y - 8 * mm, title)
y -= 12 * mm
for i, row in enumerate(rows):
    c.setFillColor(white if i % 2 == 0 else PALE)
    c.rect(x, y - rh, CONTENT_W, rh, fill=1, stroke=0)
    c.setStrokeColor(LINE)
    c.line(x, y - rh, x + CONTENT_W, y - rh)
    for j, text in enumerate(row):
        draw_text(text, x + sum(widths[:j]) + 8, y - 10 * mm, size=8.5 if j else 9, color=TEXT if j != 1 else MUTED, leading=11, max_width=widths[j] - 14)
    y -= rh
c.setFillColor(LIGHT)
c.roundRect(M, 25 * mm, CONTENT_W, 29 * mm, 5, fill=1, stroke=0)
draw_text('适合：行业新手、产品经理、求职者、咨询/投资/创业者，以及希望补齐产业和商业视角的工程师。\n不适合：希望学习算法公式与代码、寻找股票推荐，或用一份静态资料替代持续研究的人。', M + 12, 43 * mm, size=9.3, color=TEXT, leading=14, max_width=CONTENT_W - 24)
c.showPage()

# 12 CTA
c.setFillColor(NAVY)
c.rect(0, 0, W, H, fill=1, stroke=0)
c.setStrokeColor(Color(0.2, 0.65, 0.72, alpha=0.12))
c.setLineWidth(0.5)
for x in range(0, int(W), 36):
    c.line(x, 0, x, H)
for y in range(0, int(H), 36):
    c.line(0, y, W, y)
c.setFillColor(CYAN)
c.setFont('DejaVuSans-Bold', 8)
c.drawString(M, H - 36 * mm, 'GET THE FULL EDITION')
c.setFillColor(white)
c.setFont('STSong-Light', 25)
c.drawString(M, H - 57 * mm, '获取《具身智能入门》正式版')
c.setFillColor(HexColor('#C6DDE6'))
c.setFont('STSong-Light', 11)
c.drawString(M, H - 72 * mm, '120 页 PDF | 产业、公司、产品、技术与职业地图')
qx = M
qy = H - 167 * mm
qs = 63 * mm
c.setFillColor(white)
c.roundRect(qx - 8, qy - 8, qs + 16, qs + 16, 7, fill=1, stroke=0)
c.drawImage(ImageReader(str(QR)), qx, qy, qs, qs, mask='auto')
c.linkURL(BOOK_URL, (qx, qy, qx + qs, qy + qs), relative=0)
sx = M + 82 * mm
sy = H - 102 * mm
steps = ['扫码或点击进入购买页', '查看正式版介绍与当前价格', '添加微信，备注“具身智能”', '微信付款后接收正式版 PDF']
for i, step in enumerate(steps):
    c.setFillColor(CYAN)
    c.circle(sx, sy - i * 22, 8, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont('DejaVuSans-Bold', 8)
    c.drawCentredString(sx, sy - i * 22 - 3, str(i + 1))
    c.setFillColor(white)
    c.setFont('STSong-Light', 10.5)
    c.drawString(sx + 18, sy - i * 22 - 4, step)
c.setFillColor(HexColor('#A8C3CF'))
c.setFont('STSong-Light', 8.5)
c.drawString(sx, H - 164 * mm, '网站不直接收款，交易和文件交付均通过微信完成。')
bx = M
by = 57 * mm
bw = CONTENT_W
bh = 17 * mm
c.setFillColor(CYAN)
c.roundRect(bx, by, bw, bh, 6, fill=1, stroke=0)
c.setFillColor(NAVY)
c.setFont('STSong-Light', 12)
c.drawCentredString(W / 2, by + 6 * mm, 'roy-tong.github.io/book/')
c.linkURL(BOOK_URL, (bx, by, bx + bw, by + bh), relative=0)
c.setFillColor(white)
c.setFont('STSong-Light', 10)
c.drawString(M, 40 * mm, '关于作者：Roy Tong（仝夏瑞），连续创业者、产品经理。')
c.setFillColor(HexColor('#A8C3CF'))
c.setFont('STSong-Light', 8.2)
c.drawString(M, 31 * mm, '曾在平安银行、百度、科大讯飞、字节跳动和大疆工作，长期关注 AI、软件、硬件与真实商业化。')
c.setFont('STSong-Light', 7.6)
c.drawString(M, 19 * mm, '本试读版可完整、免费转发。请保留作者、书名与获取方式，不得删改后转售。')
c.showPage()

c.save()
QR.unlink(missing_ok=True)
print(f'Generated {OUT}')

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('#f2f2f2')


def draw_component(x, y, width, height, name, interfaces, color='#87CEFA'):
    rect = plt.Rectangle((x, y), width, height, fill=True, edgecolor='black', facecolor=color, linewidth=2, zorder=2)
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height - 0.5, name, ha='center', va='top', fontsize=12, fontweight='bold', zorder=3)

    # Интерфейстер
    for i, iface in enumerate(interfaces):
        ax.text(x + 0.15, y + height - 1.2 - i * 0.35, iface, ha='left', va='top', fontsize=10, zorder=3)


# Компоненттер
draw_component(1, 7, 3, 2.5, 'Frontend', ['REST API', 'WebSocket'], color='#ADD8E6')
draw_component(1, 4, 3, 2.5, 'Backend', ['Database', 'Route Optimization', 'Notification Service'], color='#B0E0E6')
draw_component(5, 7, 3, 2.5, 'Warehouse Module', ['SQL', 'Inventory API'], color='#87CEEB')
draw_component(5, 4, 3, 2.5, 'Courier Integration', ['Courier API', 'Webhook'], color='#87CEEB')
draw_component(8, 5.5, 3, 2.5, 'Analytics', ['Report API'], color='#ADD8E6')


# Стрелкалар функциясы
def draw_arrow(start, end, text=''):
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', lw=2, color='#333333'))
    if text:
        mid_x = (start[0] + end[0]) / 2
        mid_y = (start[1] + end[1]) / 2
        ax.text(mid_x, mid_y + 0.1, text, fontsize=9, ha='center', va='bottom', color='#000000')


# Взаимодействия
draw_arrow((2.5, 9.5), (2.5, 7))  # Frontend -> Backend
draw_arrow((2.5, 6.5), (6.5, 7))  # Backend -> Warehouse Module
draw_arrow((2.5, 6.5), (6.5, 5))  # Backend -> Courier Integration
draw_arrow((6.5, 7.5), (9.5, 6.5), 'Data/Reports')  # Warehouse -> Analytics
draw_arrow((6.5, 5.5), (9.5, 6.5), 'Status Updates')  # Courier -> Analytics

plt.title("Logistics Management System - Component UML Diagram", fontsize=16, fontweight='bold', color='#000080')
plt.show()

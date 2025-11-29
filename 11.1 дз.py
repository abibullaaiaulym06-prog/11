import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(14, 10))
ax.set_xlim(0, 12)
ax.set_ylim(0, 10)
ax.axis('off')
ax.set_facecolor('#f7f7f7')


def draw_class(x, y, width, height, name, attributes, methods, color='#87CEFA'):
    rect = plt.Rectangle((x, y), width, height, fill=True, edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(rect)
    # Класс атауы
    ax.text(x + width / 2, y + height - 0.5, name, ha='center', va='top', fontsize=12, fontweight='bold',
            color='#000080')

    # Атрибуттар
    attr_y_start = y + height - 1.2
    for i, attr in enumerate(attributes):
        ax.text(x + 0.15, attr_y_start - i * 0.35, attr, ha='left', va='top', fontsize=10)

    # Методы
    method_y_start = attr_y_start - len(attributes) * 0.35 - 0.3
    for j, method in enumerate(methods):
        ax.text(x + 0.15, method_y_start - j * 0.35, method + '()', ha='left', va='top', fontsize=10, color='#333333')


# Класстар
draw_class(1, 7, 3, 2.5, 'User (abstract)', ['ID', 'Name', 'Email', 'Address', 'Phone', 'Role'],
           ['register', 'login', 'update_info'], color='#ADD8E6')
draw_class(1, 4, 3, 2, 'Client', [], ['view_orders', 'make_order'], color='#B0E0E6')
draw_class(5, 7, 3, 2, 'Admin', [], ['manage_products', 'manage_orders', 'view_reports'], color='#B0C4DE')
draw_class(5, 4, 3, 2.5, 'Product', ['ID', 'Name', 'Description', 'Price', 'Stock', 'Category'],
           ['create', 'update', 'delete'], color='#87CEEB')
draw_class(1, 1, 3, 2, 'Order', ['ID', 'Date', 'Status', 'Client', 'ProductList', 'TotalAmount'],
           ['place', 'cancel', 'pay'], color='#ADD8E6')
draw_class(5, 1, 3, 2, 'Payment', ['ID', 'Type', 'Amount', 'Status', 'Date'], ['process', 'refund'], color='#B0E0E6')
draw_class(8, 4, 3, 2.5, 'Delivery', ['ID', 'Address', 'Status', 'Courier'], ['send', 'track', 'complete'],
           color='#87CEFA')


# Ассоциациялар
def draw_arrow(xy_start, xy_end):
    ax.annotate('', xy=xy_end, xytext=xy_start, arrowprops=dict(arrowstyle='-|>', lw=2, color='#333333'))


draw_arrow((2.5, 8.7), (2.5, 6.1))  # User -> Client
draw_arrow((6.5, 8.7), (6.5, 6.1))  # User -> Admin
draw_arrow((2.5, 4), (2.5, 3))  # Client -> Order
draw_arrow((2.5, 2.1), (6.5, 5.9))  # Order -> Product
draw_arrow((2.5, 2.1), (6.5, 2.9))  # Order -> Payment
draw_arrow((6.5, 2), (9.5, 5))  # Payment -> Delivery

plt.title("E-Commerce System UML Class Diagram", fontsize=18, fontweight='bold', color='#000080')
plt.show()

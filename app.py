from flask import Flask, render_template, request, redirect
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="delivery_system",
    user="postgres",
    password="335512"
)

cursor = conn.cursor()

@app.route('/')
def home():

    cursor.execute("SELECT * FROM Products")

    products = cursor.fetchall()

    return render_template('index.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():

    name = request.form['product_name']
    price = request.form['price']
    stock = request.form['stock']

    cursor.execute(
        "INSERT INTO Products(product_name, price, stock) VALUES(%s, %s, %s)",
        (name, price, stock)
    )

    conn.commit()

    return redirect('/')
@app.route('/customers')
def customers():

    cursor.execute("SELECT * FROM Customers")

    customers = cursor.fetchall()

    return render_template('customers.html', customers=customers)


@app.route('/add_customer', methods=['POST'])
def add_customer():

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    cursor.execute(
        "INSERT INTO Customers(name, email, phone) VALUES(%s, %s, %s)",
        (name, email, phone)
    )

    conn.commit()

    return redirect('/customers')

@app.route('/orders')
def orders():

    cursor.execute("""
    SELECT
        Orders.order_id,
        Customers.name,
        Orders.order_type,
        Orders.order_status,
        Orders.order_date
    FROM Orders
    JOIN Customers
    ON Orders.customer_id = Customers.customer_id
""")

    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM Customers")
    customers = cursor.fetchall()

    return render_template(
        'orders.html',
        orders=orders,
        customers=customers
    )


@app.route('/add_order', methods=['POST'])
def add_order():

    customer_id = request.form['customer_id']

    order_type = request.form['order_type']

    cursor.execute(
    """
    INSERT INTO Orders(
        customer_id,
        order_type,
        order_status
    )
    VALUES(%s, %s, %s)
    """,
    (customer_id, order_type, 'PENDING')
)

    conn.commit()

    return redirect('/orders')

@app.route('/update_status/<int:order_id>', methods=['POST'])
def update_status(order_id):

    new_status = request.form['status']

    cursor.execute(
        """
        UPDATE Orders
        SET order_status = %s
        WHERE order_id = %s
        """,
        (new_status, order_id)
    )

    conn.commit()

    return redirect('/orders')

@app.route('/order_items')
def order_items():

    cursor.execute("""
        SELECT
            Order_Items.order_item_id,
            Orders.order_id,
            Products.product_name,
            Order_Items.quantity,
            Order_Items.subtotal
        FROM Order_Items
        JOIN Orders
        ON Order_Items.order_id = Orders.order_id
        JOIN Products
        ON Order_Items.product_id = Products.product_id
    """)

    items = cursor.fetchall()

    cursor.execute("SELECT * FROM Orders")
    orders = cursor.fetchall()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    return render_template(
        'order_items.html',
        items=items,
        orders=orders,
        products=products
    )

@app.route('/add_order_item', methods=['POST'])
def add_order_item():

    order_id = request.form['order_id']
    product_id = request.form['product_id']
    quantity = int(request.form['quantity'])

    cursor.execute(
        "SELECT price FROM Products WHERE product_id = %s",
        (product_id,)
    )

    price = cursor.fetchone()[0]

    subtotal = price * quantity

    cursor.execute(
        """
        INSERT INTO Order_Items(
            order_id,
            product_id,
            quantity,
            subtotal
        )
        VALUES(%s, %s, %s, %s)
        """,
        (order_id, product_id, quantity, subtotal)
    )

    conn.commit()

    return redirect('/order_items')

if __name__ == '__main__':
    app.run(debug=True)
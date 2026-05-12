from flask import Blueprint

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        full_name = request.form.get('full_name')
        email = request.form.get('email')
        password = request.form.get('password')


        existing_user = User.query.filter_by(email=email).first()

        if existing_user:
            flash('Email already exists!', 'danger')
            return redirect(url_for('auth.register'))


        new_user = User(
            full_name=full_name,
            email=email,
            password=password
        )

        db.session.add(new_user)
        db.session.commit()


        flash('Registration successful!', 'success')

        return redirect(url_for('auth.login'))


    return render_template('auth/register.html')


@auth.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        email = request.form.get('email')
        password = request.form.get('password')


        user = User.query.filter_by(email=email, password=password).first()


        if user:

            session['user_id'] = user.id
            session['user_name'] = user.full_name

            flash('Login successful!', 'success')

            return redirect('/')

        else:
            flash('Invalid email or password!', 'danger')


    return render_template('auth/login.html')


@auth.route('/logout')
def logout():

    session.clear()

    flash('Logged out successfully!', 'success')

    return redirect(url_for('auth.login'))
from app.mini_calc import Mini_calc

class Test_mini_calc:
    def setup_method(self):
        print('Se executa la inceput')
        self.calc = Mini_calc(5, 5)

    def teardown_method(self):
        print('Se executa la final')

    def test_adunare(self):
        assert self.calc.adunare() == 10, 'Adunarea nu functioneaza corect.'

    def test_scadere(self):
        assert self.calc.scadere() == 0, 'Scaderea nu functioneaza corect.'

    def test_inmultire(self):
        assert self.calc.inmultire() == 25, 'Inmultirea nu functioneaza corect.'

    def test_impartire(self):
        assert self.calc.impartie() == 1, 'Impartirea nu functioneaza corect.'

    def test_init(self):
        assert self.calc.a == 5, 'a incorect'
        assert self.calc.b == 5, 'b incorect'


from core.models import Cliente

class ClienteModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Cliente.objects.create(id='', nombre='nombre', apellido='apellido', email='email@email.cl',  inicio='2019-11-02', fin='2019-11-20', destino='Corea Sur, Seoul', transporte= 'Bus', nacionalidad='Chile')
    
    def test_nombre_label(self):
        cliente=Cliente.objects.get(id)
        field_label=cliente._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label, 'nombre')
    
    def test_apellido_label(self):
        cliente=Cliente.objects.get(id)
        field_label=cliente._meta.get_field('apellido').verbose_name
        self.assertEquals(field_label, 'apellido')

   
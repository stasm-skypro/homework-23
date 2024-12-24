from django.db import models


class Category(models.Model):
    """Модель таблицы Категории [товаров]."""
    name = models.CharField(max_length=100, verbose_name = "Наименование категории")
    description = models.TextField(verbose_name="Описание")

    def __repl__(self):
        """Строковое представление для разработчиков."""
        return "%s %s %s" % (self.__class__, self.name, self.description)

    def __str__(self):
        """Общее строковое представление."""
        return "%s" % self.name

    class Meta:
        verbose_name ="Категория товара"
        verbose_name_plural = "Категории товаров"
        ordering = ["name",]


class Product(models.Model):
    """Модель таблицы Товар."""
    product = models.CharField(max_length=150, verbose_name="Наименование товара")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="goods")
    price = models.FloatField(null=False, default=1.0, verbose_name="Цена товара")
    created_at = models.DateField(verbose_name="Дата производства")
    changed_at = models.DateField(verbose_name="Дата последнего изменения")

    def __repl__(self):
        """Строковое представление для разработчиков."""
        return "%s %s %s %s %s" % (self.__class__,
                                   self.product,
                                   self.category,
                                   self.price,
                                   self.created_at)

    def __str__(self):
        """Общее строковое представление."""
        return "%s %s" % (self.product, self.price)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["product", "price",]

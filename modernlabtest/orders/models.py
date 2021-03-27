# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class ConstanceConfig(models.Model):
    key = models.CharField(unique=True, max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'constance_config'


class CouponsCampaign(models.Model):
    name = models.CharField(unique=True, max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'coupons_campaign'


class CouponsCoupon(models.Model):
    value = models.IntegerField()
    code = models.CharField(unique=True, max_length=30)
    type = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    valid_until = models.DateTimeField(blank=True, null=True)
    campaign = models.ForeignKey(CouponsCampaign, models.DO_NOTHING, blank=True, null=True)
    user_limit = models.IntegerField()
    redeem_count = models.IntegerField()
    redeem_limit = models.IntegerField(blank=True, null=True)
    criteria = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'coupons_coupon'


class CouponsCouponuser(models.Model):
    redeemed_at = models.DateTimeField(blank=True, null=True)
    coupon = models.ForeignKey(CouponsCoupon, models.DO_NOTHING)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('OrdersOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons_couponuser'
        unique_together = (('coupon', 'user'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSummernoteAttachment(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    file = models.CharField(max_length=100)
    uploaded = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_summernote_attachment'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, models.DO_NOTHING)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class FilerClipboard(models.Model):
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboard'


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey('FilerFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.IntegerField(db_column='_file_size', blank=True, null=True)  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    polymorphic_ctype = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_file'


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'


class FilerImage(models.Model):
    file_ptr = models.OneToOneField(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.IntegerField(db_column='_height', blank=True, null=True)  # Field renamed because it started with '_'.
    field_width = models.IntegerField(db_column='_width', blank=True, null=True)  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filer_image'


class FilerThumbnailoption(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    crop = models.BooleanField()
    upscale = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'filer_thumbnailoption'


class FormulasFormula(models.Model):
    name = models.CharField(max_length=20)
    reference = models.CharField(max_length=20)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    chapter = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formulas_formula'
        unique_together = (('name', 'reference'),)


class FormulasFormulaline(models.Model):
    quantity = models.DecimalField(max_digits=7, decimal_places=1)
    formula = models.ForeignKey(FormulasFormula, models.DO_NOTHING)
    herb_category = models.ForeignKey('HerbsHerbcategory', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'formulas_formulaline'
        unique_together = (('formula', 'herb_category'),)


class FormulasProduct(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    category = models.ForeignKey('FormulasProductcategory', models.DO_NOTHING)
    description = models.CharField(max_length=256)
    sub_type = models.CharField(max_length=32)
    price = models.IntegerField()
    package = models.ForeignKey('FormulasProductpackage', models.DO_NOTHING)
    ingredients = models.CharField(max_length=256, blank=True, null=True)
    in_stock = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'formulas_product'
        unique_together = (('category', 'sub_type', 'package', 'in_stock'),)


class FormulasProductcategory(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=256, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'formulas_productcategory'


class FormulasProductpackage(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    price = models.IntegerField()
    image = models.CharField(max_length=100, blank=True, null=True)
    weight = models.CharField(max_length=32, blank=True, null=True)
    order_unit = models.SmallIntegerField()
    package_unit = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'formulas_productpackage'


class HerbsHerb(models.Model):
    in_stock = models.BooleanField()
    price_per_unit = models.IntegerField()
    description = models.CharField(max_length=256, blank=True, null=True)
    source = models.CharField(max_length=10, blank=True, null=True)
    supplier = models.CharField(max_length=15, blank=True, null=True)
    herb_category = models.ForeignKey('HerbsHerbcategory', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'herbs_herb'
        unique_together = (('herb_category', 'price_per_unit', 'description', 'source', 'in_stock', 'supplier'),)


class HerbsHerbcategory(models.Model):
    name = models.CharField(max_length=10)
    contraindications = models.TextField()  # This field type is a guess.
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'herbs_herbcategory'


class NotificationsNotification(models.Model):
    category = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    should_popup = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'notifications_notification'


class OrdersContact(models.Model):
    user_type = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    mobile_number = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'orders_contact'


class OrdersDeliveryinvoice(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    invoice_excel = models.ForeignKey(FilerFile, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_deliveryinvoice'


class OrdersOrder(models.Model):
    delivery_infos_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    delivery_requests = models.CharField(max_length=256, blank=True, null=True)
    invoice_no = models.CharField(max_length=20, blank=True, null=True)
    receiver = models.ForeignKey(OrdersContact, models.DO_NOTHING, blank=True, null=True)
    sender = models.ForeignKey(OrdersContact, models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    status = models.CharField(max_length=32)
    delivery_amount = models.IntegerField(blank=True, null=True)
    extra_delivery_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders_order'


class OrdersOrderstatuslog(models.Model):
    status = models.CharField(max_length=50)
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    quantity = models.SmallIntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'orders_orderstatuslog'


class OrdersUserdeliveryrequest(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    message = models.CharField(max_length=256, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_userdeliveryrequest'
        unique_together = (('user', 'message'),)


class PaymentsPayment(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    status_changed = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(max_length=100)
    imp_uid = models.CharField(max_length=32, blank=True, null=True)
    merchant_uid = models.CharField(max_length=35, blank=True, null=True)
    pg_provider = models.CharField(max_length=32, blank=True, null=True)
    pay_method = models.CharField(max_length=32)
    response = models.TextField(blank=True, null=True)
    order = models.OneToOneField(OrdersOrder, models.DO_NOTHING)
    discount = models.IntegerField()
    fail_reason = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payments_payment'


class PaymentsPaymentlog(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    amount = models.IntegerField()
    status = models.CharField(max_length=100)
    imp_uid = models.CharField(max_length=32, blank=True, null=True)
    merchant_uid = models.CharField(max_length=35, blank=True, null=True)
    pg_provider = models.CharField(max_length=32, blank=True, null=True)
    pay_method = models.CharField(max_length=32)
    response = models.TextField(blank=True, null=True)
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    payment = models.ForeignKey(PaymentsPayment, models.DO_NOTHING, blank=True, null=True)
    discount = models.IntegerField()
    fail_reason = models.TextField(blank=True, null=True)
    status_changed = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments_paymentlog'


class PrescriptionsPrescription(models.Model):
    name = models.CharField(max_length=20)
    base_formula = models.ForeignKey(FormulasFormula, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING)
    additional_requests = models.TextField(blank=True, null=True)
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING, blank=True, null=True)
    patient_instructions = models.TextField(blank=True, null=True)
    tangjeon_setting = models.OneToOneField('PrescriptionsTangjeonsetting', models.DO_NOTHING, blank=True, null=True)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    total_herb_price = models.IntegerField(blank=True, null=True)
    total_herb_weight = models.DecimalField(max_digits=8, decimal_places=1, blank=True, null=True)
    water_volume = models.IntegerField(blank=True, null=True)
    is_removed = models.BooleanField()
    patient_name = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'prescriptions_prescription'


class PrescriptionsPrescriptionline(models.Model):
    quantity = models.DecimalField(max_digits=6, decimal_places=1)
    herb = models.ForeignKey(HerbsHerb, models.DO_NOTHING)
    prescription = models.ForeignKey(PrescriptionsPrescription, models.DO_NOTHING)
    created = models.DateTimeField()
    modified = models.DateTimeField()
    line_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions_prescriptionline'
        unique_together = (('herb', 'prescription'),)


class PrescriptionsPrescriptionproductline(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    quantity = models.SmallIntegerField()
    line_price = models.IntegerField(blank=True, null=True)
    prescription = models.ForeignKey(PrescriptionsPrescription, models.DO_NOTHING)
    product = models.ForeignKey(FormulasProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prescriptions_prescriptionproductline'
        unique_together = (('prescription', 'product'),)


class PrescriptionsSettingcode(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    name = models.CharField(max_length=32, blank=True, null=True)
    value = models.SmallIntegerField()
    category = models.CharField(max_length=32)
    code = models.CharField(max_length=32, blank=True, null=True)
    image = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescriptions_settingcode'


class PrescriptionsTangjeonsetting(models.Model):
    tangjeon_method = models.ForeignKey(PrescriptionsSettingcode, models.DO_NOTHING)
    chub_num = models.SmallIntegerField()
    pack_num = models.SmallIntegerField()
    pack_volume = models.SmallIntegerField()
    pack_type = models.ForeignKey(PrescriptionsSettingcode, models.DO_NOTHING)
    box_type = models.ForeignKey(PrescriptionsSettingcode, models.DO_NOTHING)
    joje_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prescriptions_tangjeonsetting'


class PrescriptionsTangjeonsettingTangjeonOption(models.Model):
    tangjeonsetting = models.ForeignKey(PrescriptionsTangjeonsetting, models.DO_NOTHING)
    settingcode = models.ForeignKey(PrescriptionsSettingcode, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'prescriptions_tangjeonsetting_tangjeon_option'
        unique_together = (('tangjeonsetting', 'settingcode'),)


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'


class ThumbnailKvstore(models.Model):
    key = models.CharField(primary_key=True, max_length=200)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'thumbnail_kvstore'


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    email = models.CharField(unique=True, max_length=256)
    username = models.CharField(max_length=15)
    license_number = models.CharField(unique=True, max_length=6, blank=True, null=True)
    mobile_number = models.CharField(unique=True, max_length=15)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    auth_image_url = models.CharField(max_length=100, blank=True, null=True)
    payment_type = models.IntegerField()
    receive_email = models.IntegerField()
    receive_sms = models.IntegerField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    role = models.IntegerField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    default_tangjeon_setting = models.OneToOneField(PrescriptionsTangjeonsetting, models.DO_NOTHING, blank=True, null=True)
    default_contact = models.OneToOneField(OrdersContact, models.DO_NOTHING, blank=True, null=True)
    is_authorized = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class UsersUserpaymentinfo(models.Model):
    created = models.DateTimeField()
    modified = models.DateTimeField()
    card_number = models.CharField(max_length=32, blank=True, null=True)
    user = models.ForeignKey(UsersUser, models.DO_NOTHING)
    card_name = models.CharField(max_length=32, blank=True, null=True)
    customer_uid = models.CharField(max_length=64, blank=True, null=True)
    is_default = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'users_userpaymentinfo'

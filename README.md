# List of Contributors
- Rosalia D'Alessandro, Telecom Italia

# SiGploit
SiGploit a signaling security testing framework dedicated to Telecom Security professionals and reasearchers to pentest and exploit vulnerabilites in the signaling protocols used in mobile operators regardless of the geneartion being in use.
SiGploit aims to cover all used protocols used in the operators interconnects SS7, GTP (3G), Diameter (4G) or even SIP for IMS and VoLTE infrastructures used in the access layer and SS7 message encapsulation into SIP-T.
Recommendations for each vulnerability will be provided to guide the tester and the operator the steps that should be done to enhance their security posture

SiGploit is developed on several versions

Note: In order to test SS7 attacks, you need to have an SS7 access or you can test in the virtual lab with the provided server sides of the attacks, the used values are provided.

  Version 1: SS7
  -------------
  SiGploit will initially start with SS7 vulnerabilities providing the messages used to test the below attacking scenarios
    A- Location Tracking
    B- Call and SMS Interception
    C- Fraud
  
  Version 2: GTP
  ------------
  This Version will focus on the data roaming attacks that occur on the IPX/GRX interconnects.
  
  Version 3: Diameter
  -----------------
  This Version will focus on the attacks occurring on the LTE roaming interconnects using Diameter as the signaling protocol.
  
  Version 4: SIP
  ------------
  This is Version will be concerned with SIP as the signaling protocol used in the access layer for voice over LTE(VoLTE) and IMS infrastructure.
  Also, SIP will be used to encapsulate SS7 messages (ISUP) to be relayed over VoIP providers to SS7 networks taking advantage of SIP-T protocol, a protocol extension for SIP to provide intercompatability between VoIP and SS7 networks
  
  Version 5: Reporting
  ------------------
  This last Version will introduce the reporting feature. A comprehensive report with the tests done along with the recommendations provided for each vulnerability that has been exploited.
  
    BETA Version of SiGploit will have the Location Tracking attacks of the SS7 phase 1

## Installation and requirements
The requirements for this project are:

    1) Python 2.7
    2) Java version 1.7 +
    3) Linux machine (Windows doesnt support SCTP)

To run use

    https://github.com/HN1A/sigploit-ss7.git
    cd sigploit-ss7
    
    python sigploit.py
    
   -----------------------
   
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



# sample script to get list of apps by vendor id

import requests
import json

# vendor_nm = {'//SEIBERT/MEDIA - AppAnvil': ['1217680'], '//SEIBERT/MEDIA GmbH': ['23019'], '2improveIT': [
# '1213523'], 'ACA IT-Solutions': ['1210753'], 'ACEDEMAND IT Consulting Services': ['1210726'], 'ADON': ['1212489'],
# 'ADONWEB': ['1214052'], 'ADWEB Software': ['1211262'], 'AELBOX': ['1215786'], 'AELBOX Ltd.': ['1215785'],
# 'AIM - Agile IT Management': ['1213191'], 'AL Software': ['1216407'], 'General Software': ['1216555'],
# 'IBM Rational Software': ['984013'], 'ALMBASE': ['1215218'], 'ASK Software': ['23324'], 'AWS': ['1217330'],
# 'AWSEC2SpotFleet': ['1215143'], 'Absolute Technology Solutions': ['1216237'], 'Accxia': ['1214007'],
# 'Acid Oranges': ['1215767'], 'Actonic GmbH': ['1214306'], 'Add-On Experts Center': ['1214502'], 'Adips Sp. z o.o.':
# ['1213193'], 'Adobe Inc.': ['1216060'], 'Agile Better, Inc.': ['1213948'], 'Aha! Labs Inc': ['1210950'],
# 'Alan Hohn': ['1212548'], 'Alexandr Pustovit': ['1211772'], 'Alkaes Consulting': ['6238'], 'Allenta Consulting S.L.
# (CIF ESB15974553)': ['1211837'], 'AlutusTech': ['1213888'], 'Ambit Security': ['1215541'], 'Amir Toole': [
# '1215715'], 'Amir Toole - CWI': ['1210715'], 'Amrut Software Pvt Ltd': ['1214843'], 'Andrey Kostin': ['1213100'],
# 'Andrey Kostin2': ['1213841'], 'Andrey V Markelov': ['1210741'], 'Anna Tikhonova': ['1213103'],
# 'Apio': ['1215878'], 'Apps and Magic': ['1215865'], 'AppsDelivered': ['1216797'], 'Apwide': ['1211423'],
# 'Artezio': ['1210798'], 'Ascend Integrated': ['1215938'], 'Ascensio System SIA': ['1215029'], 'Assemblient': [
# '1214588'], 'AtlaZon': ['1180729'], 'Atlas team': ['1215089'], 'AtlasSoft': ['1215494'], 'AutoTestingTools Software
# and Services pty ltd': ['1212370'], 'Autodesk Inc.': ['1214553'], 'Automation Consultants Ltd': ['1213613'],
# 'Automic Software Gmbh': ['1214088'], 'AvR': ['1210781'], 'Favro AB': ['1213383'], 'Favro Test': ['1213540'],
# 'Thibaut Wavreille': ['1211200'], 'Avant': ['1211563'], 'Baloise Group': ['1211530'], 'Stefan Bauer': ['774266'],
# 'Belmont Technology Pty Ltd': ['1211357'], 'Benryan Software Inc.': ['1211578'], 'Bhushan Nagaraj': ['1210767'],
# 'Bilith (Zoho apps)': ['1218376'], 'Bit-Booster Software': ['1212789'], 'Bitium, Inc': ['1211482'], 'Black Duck
# Software': ['1211315'], 'Black Duck Software, Inc.': ['1213384'], 'Black Rabbit LLC': ['1211661'], 'Boll.IT BV': [
# '1213297'], 'Boris Diakur': ['1212221'], 'Boris Jockov': ['1212488'], 'Brightsoft Apps': ['28527'], 'Broken Build
# Lab': ['1213172'], 'Bruho': ['1210938'], 'Bug Potion': ['1210790'], 'BugsIO Solutions': ['36242'], 'Bunney Apps': [
# '1210610'], 'Buzz Plugins': ['1215043'], 'ByteSource Technology Consulting GmbH': ['1211960'], 'CHECKMARX': [
# '1211668'], 'CHROBRUS': ['1211609'], 'CLEITO': ['1212339'], 'CTO Kit': ['1213355'], 'CURVC Corp.': ['1213901'],
# 'Candylio Software Pte. Ltd.': ['1211771'], 'Carolyn Van Slyck': ['1211016'], 'Catch Software': ['6257'],
# 'Celeste Creative Solutions': ['1211610'], 'Celigo, Inc.': ['1212846'], 'Change Vision, Inc.': ['814906'],
# 'Christian Galsterer': ['1211799'], 'Cinergix': ['326567'], 'Citrix': ['1210758'], 'Clarios Technology': [
# '1210642'], 'CloseIT s.r.o.': ['43259'], 'CloudBees': ['1215828'], 'Coded Poetry': ['1213835'], 'Codeletic': [
# '1216606'], 'Coldfire': ['1211140'], 'CollabNet Inc': ['1212554'], 'Commerce Computing Limited': ['1211845'],
# 'Communardo Labs': ['1210722'], 'Alexandra Topoloaga (cPrime)': ['1215478'], 'CrazyCookieCoders': ['823183'],
# 'Cucumber, a SmartBear company': ['1211678'], 'DEISER LABS': ['1213485'], 'David Erickson': ['1211440'],
# 'David Erickson old': ['391551'], 'David Koudela Inc.': ['1210639'], 'David Ortiz Montero': ['1213812'],
# 'David Simpson Apps': ['15071'], 'DevSamurai': ['1216701'], 'Devart': ['1212981'], 'DevartDbForge': ['1217993'],
# 'Develocenter': ['1212381'], 'Devexperts': ['1215045'], 'Device42': ['1212225'], 'Dieter Wimberger': ['1210579'],
# 'DigiTime OU': ['1211717'], 'DigiXperience': ['1215660'], 'Digital Ray': ['1216062'], 'Discoman Development': [
# '1211083'], 'Dmitry Deriugin': ['1215652'], '_Dmitry Deriugin_': ['1215331'], 'Documentation Toolkit': ['1216621'],
# 'DragonSoft': ['1215035'], 'Drunken Dev': ['34634'], 'E7 Solutions': ['1211053'], 'EDAG Production Solutions GmbH &
# Co. KG': ['1214150'], 'EEA communication solutions': ['22964'], 'EF Learning Labs': ['1210773'], 'EISOFT': [
# '1213905'], 'EPAM Systems, Inc.': ['1211227'], 'EPOS CAT GmbH': ['1213604'], 'Eamonn McEvoy': ['1212552'],
# 'Easysecrets': ['5069'], 'Ecliptic Technologies, Inc.': ['11979'], 'EduBrite Systems Inc.': ['27672'],
# 'Edward A Webb': ['1017039'], '5 Elements Creative': ['1218280'], 'SD Elements': ['1210661'], 'Emin Üzümlüoğlu': [
# '1213263'], 'Empyra': ['1213530'], 'Enisra': ['1211692'], 'Equion Consulting Limited': ['954004'], 'Eric Stokes': [
# '1211758'], 'Evercode': ['1212908'], 'FRONTCLOUD': ['1211968'], 'FSOFT - FPT Software': ['1215738'],
# 'FindOut Technologies AB': ['1215197'], 'Foreach': ['1210804'], 'Forty8Fifty Labs': ['1213512'], 'Fulstech': [
# '1212817'], 'Gebsun Gebsun': ['1210643'], 'Gebsun Labs': ['1214717'], 'Gebsun Solutions': ['1215156'], 'Gebsun111':
# ['1210746'], 'Gliffy Inc.': ['1215048'], 'Wang_Gliffy': ['1212690'], 'Globo Solutions': ['1216070'],
# 'Go2Group K.K.': ['20755'], 'GreenElephant': ['1215928'], 'GreenElephant1': ['1213007'], 'Greenyloop': ['1213732'],
# 'Grovr': ['1214776'], 'Gtmhub': ['1214742'], 'Gumvillage': ['1210690'], 'Gurock': ['37811'], 'H.S. PractiTest
# Ltd.': ['1210724'], 'HUB.RE': ['1216239'], 'Haithem Souala': ['1214073'], 'Henix': ['1212166'], 'henix squash': [
# '1217243'], 'Herbert Kruitbosch': ['1213210'], 'Herzum': ['1210816'], 'Hivestone': ['1214547'], 'Hugh McManus': [
# '1212193'], 'Hugh McManusCS': ['492227'], 'Hutuleac Iulius': ['1212307'], 'ILA eSolution': ['1216055'], 'IT IDEA':
# ['1210978'], 'IXPERTA s.r.o.': ['1215550'], 'InLabs': ['1212086'], 'InVision': ['1213393'], 'Incloud GmbH': [
# '1212423'], 'Infosysta Test': ['1214644'], 'Infusion': ['1212031'], 'Orange Infusion LLC': ['1217726'], 'Innovura':
# ['1217408'], 'Isos Technology.': ['1210845'], 'Itransition Group': ['1215069'], 'JADP': ['1213261'], 'Jaanga': [
# '1215973'], 'Jamie Echlin': ['5263'], 'JavaMelody': ['20906'], 'JetBrains': ['1211898'], 'JiBrok': ['1216083'],
# 'Johannes  Heger': ['1212081'], 'Junoe': ['1212089'], 'Justin Shapiro': ['14417'], 'Justinmind': ['1214267'],
# 'K15t Labs': ['1210915'], 'KC Integrations': ['1211876'], 'Karthik Venkataraman': ['1213157'], 'Katalon Studio -
# Best Test Automation Solution': ['1214790'], 'Kepler Technologies': ['1216919'], 'Kepler Technologies SARL': [
# '1214495'], 'Keysight Technologies': ['1211991'], 'Kickdrum Technology Group LLC': ['1212861'], 'Kirill Shashov': [
# '1215295'], 'Kod Gemisi': ['1211855'], 'Kolibri Digital': ['1214746'], 'Koncis': ['1212553'], 'Koncis ApS': [
# '1211265'], 'Kyle Nicholls': ['1211725'], 'Lamproite': ['1217185'], 'Lasse Langhorn': ['1212528'], 'Lean Walk': [
# '1213770'], 'LeanIX': ['1216242'], 'Lee Shin Woo': ['1214296'], 'Lev Aminov': ['1216332'], 'Lewe.com': ['1214991'],
# 'Lime Trees': ['1214578'], 'LuxPlugins': ['1215514'], 'M20 Technology LLC': ['1212024'], 'MESILAT LIMITED': [
# '1213180'], 'MKTiers': ['1217108'], 'ManageEngine': ['1214812'], 'Marc Trey': ['1210864'], 'Marvel': ['1213758'],
# 'Marvelution B.V.': ['11178'], 'Maryna Prystrom': ['1211558'], 'Materna Information & Communications SE': [
# '1213807'], 'Matthew Jensen': ['36109'], 'Maximilian Porzelt': ['1216966'], 'MeetMe, Inc.': ['1210568'],
# 'Meetical': ['1217198'], 'Meetical.io': ['1217019'], 'Metova': ['1211385'], 'Michiel Roos': ['1213829'],
# 'Micro Focus': ['1211166'], 'Micro Focus Fortify': ['1216849'], 'MicroFocus Ltd.': ['1214188'], 'Microsoft Office
# 365': ['1214563'], 'Mike Kessler': ['1212891'], 'Mike Stead': ['1214958'], 'Milestone Solutions': ['1216088'],
# 'Mirketa Inc': ['1214225'], 'Miro - online collaborative whiteboard': ['1213323'], 'Mizan': ['1210565'],
# 'Mohami Staging': ['1218187'], 'Moqups': ['1212376'], 'Eernie by Move Work Forward': ['1213356'], 'Jigit by Move
# Work Forward': ['1213853'], 'PB by Move Work Forward': ['1211871'], 'Mumo Systems': ['1212550'], 'MustHave
# Technology': ['35718'], 'My.com': ['37127'], 'MyHeritage Ltd.': ['1217125'], 'NETAPSYS': ['661288'],
# 'NOW CONSULTIANS GmbH & Co. KG': ['1215679'], 'NWGG Pty Ltd': ['1213925'], 'NY Foundling': ['1211988'], 'Nara Syst
# Ltd.': ['1215335'], 'Narwhals Consulting': ['1216369'], 'Navarambh Software Pvt. Ltd. - Old': ['1215125'],
# 'Nemetschek Bulgaria': ['1212521'], 'NetworkedAssets': ['1211639'], 'NetworkedAssets GmbH': ['1210948'],
# 'New Media and Technologies Sp. z o.o.': ['1213389'], 'New Relic': ['1214969'], 'New Relic Dev': ['1214799'],
# 'New Relic, Inc.': ['1210609'], 'New Verve Consulting': ['1214638'], 'Nextup.ai - Apps for Slack': ['1214995'],
# 'Nimeko Software': ['1214558'], 'NullPointerException Systems': ['1213980'], 'ONEPOINT Projects': ['29388'],
# 'OVD Group': ['1213536'], 'Oboard Inc.': ['1216356'], 'Oleg Burmistrov': ['1210524'], 'Oliver Straesser': [
# '905616'], 'Oomnitza': ['1211891'], 'Oomnitza Inc.': ['1214595'], 'Open Source Consulting': ['1213576'],
# 'Open Source Consulting, Inc.': ['1213574'], 'Optimizory Technologies Pvt. Ltd.': ['30510'], 'Orbitz': ['1211153'],
# 'Ovyka': ['1213307'], 'PMEase Inc': ['24007'], 'PagerDuty': ['1212216'], 'PagerDuty Test Account': ['1218359'],
# 'Patrick Facheris': ['1214780'], 'Patrik Varga': ['1212574'], 'Pavel Baranchikov': ['1211708'], 'Perfect Commit': [
# '1212377'], 'Perforce Software': ['1214285'], 'Petteri Kivimäki': ['1210737'], 'Philipp Eckelmann': ['1212785'],
# 'Pineant Plugins': ['1211240'], 'Pirate Ninja Unicorn': ['1210576'], 'Pirate Ninja Unicorn II': ['1210672'],
# 'Pitronote': ['1215041'], 'Polar Shift Ltd.': ['1210550'], 'Praecipio Software': ['850362'], 'Precision Plugins': [
# '1211467'], 'Precog Software': ['1210536'], 'Prepend': ['1211294'], 'Prism Project': ['1214869'], 'ProductPlan': [
# '1213899'], 'Projektron GmbH': ['1210894'], 'ProtoShare / Astound Commerce': ['1210796'], 'QMetry Inc.': [
# '1217230'], 'Qameta Software': ['1211526'], 'Ray Barham': ['121'], 'Red Hat': ['42370'], 'Release Management': [
# '1216961'], 'Resight': ['1211980'], 'Rixter AB': ['1214651'], 'Ros Entertainment': ['1213586'], 'Rozdoum': [
# '773829'], 'Sandstorm': ['1214184'], 'Sapling Valley': ['1213440'], 'Sauce Labs': ['433496'], 'Schütze AG': [
# '1214194'], 'Scolution GmbH & Co. KG': ['1215691'], 'Sean Ford': ['1211122'], 'SecSign Technologies': ['1212526'],
# 'ServiceRocket Labs': ['1212722'], 'ServiceRocket-Test': ['1213711'], 'Shanghai Digital Talent Technology Co.,
# Ltd.': ['1214894'], 'Shinetech Software': ['1216942'], 'Shippable': ['1213143'], 'Siemens AG, Corporate
# Technology': ['582492'], 'Sistel SL': ['1214604'], 'Slie': ['1210607'], 'SmartBear QAC': ['1211884'], 'SmartDraw
# Software': ['1214917'], 'SmartDraw Software, LLC': ['1213844'], 'SmartForce': ['1217481'], 'Smateso - Smart Team
# Solutions': ['1217164'], 'SoftComply': ['1213743'], 'SoftCrts': ['1215354'], 'SoftServe': ['1213467'], 'Softlist':
# ['1215615'], 'Software Quality Lab GmbH': ['1217472'], 'Solveka': ['1066983'], 'Sonatype': ['1213691'],
# 'Sparx Systems Prolaborate': ['1215780'], 'Steffen Stamprath': ['1215126'], 'Stephan Bechter': ['1211793'],
# 'StiltSoft Labs': ['1216111'], 'Strategery Solutions BVBA': ['1210774'], 'Structurizr': ['1213399'],
# 'Sweet Bananas': ['1213300'], 'Sylvain FRANCOIS': ['44005'], 'Sylvain LAURENT': ['1212421'], 'Synack,
# Inc.': ['1216473'], 'TEMPEST': ['1217519'], 'TNG Technology Consulting GmbH': ['114'], 'Taylor Jones': ['1211822'],
# 'TeamSphere': ['1214837'], 'TeamViewer GmbH': ['1211699'], 'MyTeamlead': ['1217961'], 'Teemu Torvela': ['1211613'],
# 'Test Collab': ['1212855'], 'Test IT': ['1216761'], 'The Crust Software': ['1211608'], 'Tommer Lahat': ['1211742'],
# 'Toshihiro Sato': ['1215814'], 'TouchDown': ['1214323'], 'Transition Technologies PSC Sp. z o.o.': ['1215930'],
# 'Tricentis': ['1210533'], 'Trimble Solutions Corporation': ['1213192'], 'Unlimax': ['1210994'], 'VINC Software': [
# '1211794'], 'Valeriya Shevchenko': ['1214550'], 'Veracode': ['1214353'], 'Vestmark': ['1214715'], 'Vighnaharta': [
# '1212764'], 'Viktor Kaydalov': ['1214415'], 'Vilisoft': ['1214764'], 'Vivid Inc.': ['1211184'], 'W Knowledge': [
# '1216006'], 'White Software': ['1212758'], 'WhiteHat Security': ['1210752'], 'WhiteSource': ['1210606'],
# 'WhiteSource For Jira': ['1215414'], 'Wikistrat Inc.': ['1210855'], 'Wim Deblauwe': ['4967'], 'Wombats Corp': [
# '1214031'], 'WorkBoard Inc.': ['1217265'], 'Workfront Inc.': ['1215087'], 'XALT Business Consulting GmbH': [
# '1215937'], 'Xavier Arques': ['1212356'], 'XebiaLabs': ['677221'], 'YASSIN B': ['1216836'], 'Yaroslav Lukyanov': [
# '1212605'], 'Yiraphic': ['1215249'], 'Zendesk': ['7485'], 'acocon GmbH - business division greenique': ['1211670'],
# 'airfocus GmbH': ['1216534'], 'atSistemas': ['1211700'], 'avono AG': ['747510'], 'beecom software': ['1103495'],
# 'bit2bit Americas': ['1213273'], 'bitFit': ['1216515'], 'bitvoodoo labs': ['1213018'], 'Buddybuild - Doe Pics Hit
# Holdings ULC': ['1216687'], 'buddybuild': ['1213664'], 'celix Solutions': ['37642'], 'codeclou UG (
# haftungsbeschränkt)': ['1210693'], 'codescape - Stefan Glase': ['1215070'], 'eMundo GmbH': ['1215509'],
# 'Agile Extensions': ['1213312'], 'ElsnerMagentoExtensions': ['1213819'], 'TeamEXtension': ['1215853'], 'echocat': [
# '1211258'], 'evolu software GmbH': ['42029'], 'flaregames GmbH': ['1212206'], 'Micha Kops (hasCode.com)': [
# '22595'], 'hktxcn.com (汇科天下)': ['1213659'], 'i0in.ltd': ['1216037'], 'i4ware Software': ['30865'], 'ij-solutions UG
# (haftungsbeschränkt)': ['1216765'], 'iorad inc.': ['1212132'], 'it-economics GmbH': ['1212842'], 'it.Lab Adam
# Labus': ['1214735'], 'kyona GmbH': ['1214005'], 'limon4ick': ['1214304'], 'limon4ick-25': ['1216358'],
# 'mgm technology partners': ['1216227'], 'miniorange-test': ['1214347'], 'Mirrorlake Software': ['1211534'],
# 'openmind': ['1212025'], 'proventis GmbH': ['1212828'], 'quisapps.com': ['16343'], 'ricebean.net': ['1212039'],
# 'savignano software solutions': ['1215056'], 'scmenthusiast': ['1213337'], 'smartics': ['1211428'], 't2consult': [
# '1216212'], 'test IO': ['1214394'], 'tibe.io GmbH': ['1216779'], 'viadee Unternehmensberatung AG': ['1213394'],
# 'wirecube': ['1216136'], 'xMatters': ['1213116'], 'yWorks GmbH': ['35621'], 'zAgile': ['817771'], 'zenofx.com': [
# '1210858'], 'Øystein Gisnås': ['1212590']} vendor_nm = {'//SEIBERT/MEDIA - AppAnvil': ['1217680']} vendor_nm = {
# 'Bilith': ['1213750'], 'Bilith (GSuite apps)': ['1217380'], 'Bilith (Office 365 apps)': ['1217319'], 'Bilith (Zoho
# apps)': ['1218376'], '5 Elements Creative': ['1218280'], 'Elements': ['4952'], 'Elements.cloud': ['1218966'],
# 'SD Elements': ['1210661'], 'Midori Global Consulting Kft.': ['103'], 'ServiceRocket': ['96'], 'ServiceRocket
# Labs': ['1212722'], 'ServiceRocket-Test': ['1213711'], 'Transition Technologies PSC': ['37453'], 'Transition
# Technologies PSC Sp. z o.o.': ['1215930'], 'OBSS': ['616898']} vendor_nm = {'Adaptavist': ['81'],
# 'Vinesha Adaptavist': ['1219061'], 'ALM Works': ['7035'], 'Amoeboids Technologies Pvt Ltd': ['1211499'],
# 'APPFIRE_WWLCONNECTADDON': ['1212374'], 'Appfire Technologies, Inc.': ['24580'], 'Beecom Atlassian Apps (an Appfire
# company)': ['42620'], 'Bob Swift Atlassian Apps (an Appfire company)': ['90'], 'Botron Atlassian Apps (an Appfire
# company)': ['1210910'], 'Feed Three Atlassian Apps (an Appfire company)': ['1215927'], 'Innovalog Atlassian Apps (
# an Appfire company)': ['101'], 'Priyanka_appfire': ['1212130'], 'Wittified (an Appfire company) Customizer addons':
# ['1211501'], 'APTIS GmbH': ['1211721'], 'Artemis Software': ['84'], 'Avisi B.V.': ['16045'], 'BigBrassBand': [
# '1210545'], 'Bolo Software': ['1210571'], 'codefortynine GmbH': ['1213041'], 'Colined': ['1213040'], 'Comalatech':
# ['94'], 'Communardo Labs': ['1210722'], 'Communardo Products GmbH': ['95'], 'Alexandra Topoloaga (cPrime)': [
# '1215478'], 'Cprime': ['1211168'], 'DEISER': ['27570'], 'DEISER LABS': ['1213485'], 'Deviniti': ['39038'],
# '//SEIBERT/MEDIA - Draw.io': ['1210578'], 'draw.io AG': ['1216328'], 'Easy Agile': ['1212045'], 'eazyBI': [
# '866502'], '5 Elements Creative': ['1218280'], 'Elements': ['4952'], 'Elements.cloud': ['1218966'], 'SD Elements':
# ['1210661'], 'Gliffy': ['99'], 'Gliffy Inc.': ['1215048'], 'Wang_Gliffy': ['1212690'], 'HeroCoders': ['1215166'],
# 'K15t': ['7016'], 'K15t Custom Apps': ['1218726'], 'K15t Labs': ['1210915'], 'Lizard Brain UG': ['1211528'],
# 'Mohami': ['1211979'], 'Mohami Staging': ['1218187'], 'Eernie by Move Work Forward': ['1213356'], 'Jigit by Move
# Work Forward': ['1213853'], 'Move Work Forward': ['1213354'], 'PB by Move Work Forward': ['1211871'], 'Navarambh
# Software Pvt. Ltd.': ['1211784'], 'Navarambh Software Pvt. Ltd. - Old': ['1215125'], 'Okapya Software Solutions
# Inc.': ['1210673'], 'ProjectBalm': ['1211840'], 'QMetry': ['14074'], 'QMetry Inc.': ['1217230'], 'Refined': [
# '15228'], 'RefinedWiki': ['1218728'], 'Cucumber, a SmartBear company': ['1211678'], 'SmartBear': ['17834'],
# 'SmartBear QAC': ['1211884'], 'SoftwarePlant': ['1211388'], 'Spartez Software': ['7755'], 'StiltSoft': ['27437'],
# 'StiltSoft Labs': ['1216111'], 'Tempo': ['1210611'], 'Tempo Cloud Team': ['1211635'], 'Tempo for JIRA': ['6558'],
# 'tempo budgeting': ['1216782'], 'tempo nzhou': ['1216611'], 'ThinkTilt': ['1213227'], 'Transition Technologies': [
# '26683'], 'Transition Technologies PSC': ['37453'], 'Transition Technologies PSC Sp. z o.o.': ['1215930'],
# 'WISOFT': ['1210999'], 'Xpand IT': ['31085'], 'yasoon': ['1211722'], '55 Degrees AB': ['1216058']}
vendor_nm = {'Adaptavist': ['81']}
vendor_new_dict = {}
app_new_dict = {}
no_dc_apps_list = []

for k, v in vendor_nm.items():
    vendor_name = k
    print('Vendor Name:', vendor_name)
    vendor_id = v[0]
    base_url = 'https://marketplace.atlassian.com/rest/2/addons'
    r_url = ''.join([base_url, '/', 'vendor', '/', vendor_id])
    r_url = '?'.join([r_url, 'hosting=datacenter'])
    # print (url)
    r = requests.get(r_url)
    r_json = json.loads(r.text)
    print(r_json)
    # print ('Count:' ,r_json['count'])
    if r_json['count'] != 0:
        # print (len(r_json['_embedded']['addons']))
        for n in range(0, len(r_json['_embedded']['addons'])):
            app_list = []
            # print (r_json['_embedded']['addons'][n]['name'])
            app_key = r_json['_embedded']['addons'][n]['key']
            d_url = ''.join([base_url, '/', app_key, '/', 'distribution'])
            # print (d_url)
            d = requests.get(d_url)
            d_json = json.loads(d.text)
            if 'downloads' in d_json:
                num_dl = d_json['downloads']
            else:
                num_dl = 0
            if 'totalInstalls' in d_json:
                num_total_installs = d_json['totalInstalls']
            else:
                num_total_installs = 0
            if 'totalUsers' in d_json:
                num_users = d_json['totalUsers']
            else:
                num_users = 0
            p_url = ''.join([base_url, '/', app_key, '/', 'pricing', '/', 'datacenter', '/', 'live'])
            # print (p_url)
            p = requests.get(p_url)
            # print (p.status_code)
            # print (type (p.status_code))
            # print (p_json)
            if p.status_code == 404:
                p_type = 'Free or Unknown'
                # print (p_type)
            else:
                p_json = json.loads(p.text)
                p_type = p_json['items'][0]['licenseType']
            app_list.extend(
                (r_json['_embedded']['addons'][n]['key'], vendor_name, num_dl, num_total_installs, num_users, p_type))
            app_new_dict[r_json['_embedded']['addons'][n]['name']] = app_list
            # app_list.append(r_json['_embedded']['addons'][n]['key'])
            # vendor_new_dict[vendor_name] = app_list
    else:
        print('No DC Apps')
        no_dc_apps_list.append(vendor_name)
# print (vendor_new_dict)
# print (app_new_dict)
# print (len(app_new_dict))

for a in app_new_dict:
    alist = app_new_dict[a]
    print("{}\t{}".format(a, alist))

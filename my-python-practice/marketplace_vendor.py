# sample script to get top vendor status in Atlassian marketplace
import requests
import json

vendor_list = ['Adaptavist', 'ALM Works', 'Amoeboids Technologies', 'Appfire', 'APTIS GmbH', 'Artemis Software',
               'Avisi', 'Balsamiq Studios', 'BigBrassBand', 'Bolo Software', 'codefortynine GmbH', 'Colined',
               'Comalatech', 'Communardo', 'CPrime', 'DEISER', 'Deviniti', 'DRAW.io', 'Easy Agile', 'eazyBI',
               'Elements', 'Gliffy', 'HeroCoders', 'Innovalog', 'K15t', 'Lizard Brain UG', 'Mohami',
               'Move Work Forward', 'Navarambh Software', 'Okapya Software Solutions', 'ProjectBalm', 'QMetry',
               'Refined', 'Resolution RNS', 'Smartbear', 'SoftwarePlant', 'Spartez Software', 'StiltSoft', 'Tempo',
               'ThinkTilt', 'Transition Technologies', 'WISOFT', 'Xpand IT', 'Yasoon', '55 Degrees AB']
# vendor_list = ['//SEIBERT/MEDIA', '//SEIBERT/MEDIA - AppAnvil', '//SEIBERT/MEDIA - Draw.io', '//SEIBERT/MEDIA -
# Junovi', '2improveIT', '55 Degrees AB', 'ACA IT-Solutions', 'ACEDEMAND IT Consulting Services', 'ADON',
# 'ADWEB Software', 'AELBOX', 'AIM - Agile IT Management', 'AL Software', 'ALM Works', 'ALMBASE', 'APTIS GmbH',
# 'ASK Software', 'AWS', 'Absolute Technology Solutions', 'Accxia', 'Acid Oranges', 'Actonic GmbH', 'Adaptavist',
# 'Add-On Experts Center', 'Addonrock Sp. z o.o.', 'Addteq Inc', 'Adips Sp. z o.o.', 'Adobe Inc.', 'Agile Better,
# Inc.', 'Agilis LT', 'Aha! Labs Inc', 'Akeles Consulting', 'Alan Hohn', 'Alexandr Pustovit', 'Alkaes Consulting',
# 'Allenta Consulting S.L. (CIF ESB15974553)', 'Alpha Serve', 'AlutusTech', 'Ambit Security', 'Amir Toole',
# 'Amoeboids Technologies Pvt Ltd', 'Amrut Software Pvt Ltd', 'Andrey Kostin', 'Andrey V Markelov', 'Anna Tikhonova',
# 'Apio', 'AppLiger', 'Apps and Magic', 'AppsDelivered', 'Appsvio LLC', 'Apwide', 'Arsenale', 'Artemis Software',
# 'Artezio', 'Ascend Integrated', 'Ascensio System SIA', 'Assemblient', 'AtlaZon', 'Atlas Authority', 'Atlas team',
# 'AtlasSoft', 'AutoTestingTools Software and Services pty ltd', 'Autodesk Inc.', 'Automation Consultants',
# 'Automic Software Gmbh', 'AvR', 'Avant', 'Avisi B.V.', 'Baloise Group', 'Balsamiq Studios, LLC', 'Bauer',
# 'Belmont Technology Pty Ltd', 'Benryan Software Inc.', 'Bhushan Nagaraj', 'BigBrassBand', 'Bilith', 'Bilith (GSuite
# apps)', 'Bit-Booster Software', 'Bitium, Inc', 'Black Duck Software', 'Black Rabbit LLC', 'Bob Swift Atlassian Apps
# (an Appfire company)', 'Bobronix', 'Boll.IT BV', 'Bolo Software', 'Boris Diakur', 'Boris Jockov',
# 'Botron Software', 'Brightsoft Apps', 'Brikit', 'BrizoIT', 'Broken Build', 'Bruho', 'Bug Potion',
# 'BugsIO Solutions', 'Bunney Apps', 'Buzz Plugins', 'ByteSource Technology Consulting GmbH', 'CHECKMARX',
# 'CHROBRUS', 'CLEITO', 'CTO Kit', 'CURVC Corp.', 'Candylio Software Pte. Ltd.', 'Capital City Consultants',
# 'Carolyn Van Slyck', 'Catch Software', 'Celeste Creative Solutions', 'Celigo, Inc.', 'Cenote', 'Change Vision,
# Inc.', 'Chinese Technical Support', 'Christian Galsterer', 'Cinergix', 'Citrix', 'Clarios Technology',
# 'CloseIT s.r.o.', 'CloudBees', 'Coded Poetry', 'Codeletic', 'Coldfire', 'Colined', 'CollabNet Inc', 'CollabSoft',
# 'Comalatech', 'Commerce Computing Limited', 'Communardo Labs', 'Communardo Products GmbH', 'CoreSoft Labs',
# 'Cprime', 'CrazyCookieCoders', 'Cucumber, a SmartBear company', 'DEISER', 'DEISER LABS', 'David Erickson',
# 'David Koudela Inc.', 'David Ortiz Montero', 'David Simpson Apps', 'Decadis AG', 'DevOpsSystems Mueller',
# 'DevSamurai', 'Devart', 'Develocenter', 'Devexperts', 'Device42', 'Deviniti', 'Dieter Wimberger', 'DigiTime OU',
# 'DigiXperience', 'Digital Ray', 'Digital Toucan', 'Discoman Development', 'Dmitrii Apanasevich', 'Dmitry Deriugin',
# 'Documentation Toolkit', 'DragonSoft', 'Drunken Dev', 'E7 Solutions', 'EDAG Production Solutions GmbH & Co. KG',
# 'EEA communication solutions', 'EF Learning Labs', 'EISOFT', 'EPAM Systems, Inc.', 'EPOS CAT GmbH', 'EPS Software
# Engineering AG', 'Eamonn McEvoy', 'Easy Agile', 'Easysecrets', 'Ecliptic Technologies, Inc.', 'EduBrite Systems
# Inc.', 'Edward A Webb', 'Elements', 'EliteSoft', 'Emin Üzümlüoğlu', 'Empyra', 'Enhancera, LLC', 'Enisra',
# 'Equion Consulting Limited', 'Eric Stokes', 'Evercode', 'Everit Kft.', 'FRONTCLOUD', 'FSOFT - FPT Software',
# 'Favro AB', 'FindOut Technologies AB', 'Foreach', 'Forty8Fifty Labs', 'Frank Polscheit', 'Fulstech', 'GLiNTECH',
# 'Gebsun', 'Gebsun Software', 'Geekminds', 'GetConnected', 'Gliffy', 'Globo Solutions', 'Go2Group', 'GreenElephant',
# 'Greenyloop', 'Grovr', 'Gtmhub', 'Gumvillage', 'Gurock', 'H.S. PractiTest Ltd.', 'HUB.RE', 'Haithem Souala',
# 'Henix', 'Herbert Kruitbosch', 'Herzum', 'Hexygen Inc.', 'Hindsight Software Ltd', 'Hivestone',
# 'Holger Schimanski', 'Hugh McManus', 'Hutuleac Iulius', 'ILA eSolution', 'IT IDEA', 'IXPERTA s.r.o.', 'InLabs',
# 'InVision', 'Incloud GmbH', 'Infosysta', 'Infusion', 'Innovalog', 'Innovura', 'Inprowiser Engineering', 'Inversion
# Point LLC', 'Isos Technology.', 'Itransition Group', 'Izymes Pty Ltd', 'J-Tricks', 'JADP', 'JSoftware', 'Jaanga',
# 'Jamie Echlin', 'JavaMelody', 'JetBrains', 'JiBrok', 'Johannes  Heger', 'Junoe', 'Justin Shapiro', 'Justinmind',
# 'K15t', 'K15t Labs', 'KC Integrations', 'Kantega SSO', 'Karthik Venkataraman', 'Katalon Studio - Best Test
# Automation Solution', 'Kepler Technologies', 'Keysight Technologies', 'Kickdrum Technology Group LLC',
# 'Kirill Shashov', 'Kod Gemisi', 'Kolibri Digital', 'Koncis', 'Koncis ApS', 'KontextWork', 'Kupper Software',
# 'Kyle Nicholls', 'Köstebek Teknoloji', 'LB Consulting Group', 'Lamproite', 'Lasse Langhorn', 'Lean Walk', 'LeanIX',
# 'Lee Shin Woo', 'Lev Aminov', 'Lewe.com', 'Lime Trees', 'Lively Apps', 'Lizard Brain UG', 'Lucidchart',
# 'LuxPlugins', 'M20 Technology LLC', 'MESILAT LIMITED', 'META-INF KFT', 'MKTiers', 'MOEWE', 'MORESIMP',
# 'ManageEngine', 'Marc Trey', 'Marketplace Expert SL', 'Marvel', 'Marvelution B.V.', 'Maryna Prystrom',
# 'Materna Information & Communications SE', 'Matthew Jensen', 'Maximilian Porzelt', 'MeetMe, Inc.', 'Meetical',
# 'Metova', 'Mibex Software GmbH', 'Michiel Roos', 'Micro Focus', 'MicroFocus Ltd.', 'Microsoft Office 365',
# 'Midori Global Consulting Kft.', 'Mike Kessler', 'Mike Stead', 'Milestone Solutions', 'Mindville', 'Mirketa Inc',
# 'Miro - online collaborative whiteboard', 'Mizan', 'MobilityStream, LLC', 'Mohami', 'Moqups', 'MoroSystems,
# s.r.o.', 'Move Work Forward', 'Mumo Systems', 'MustHave Technology', 'My.com', 'MyHeritage Ltd.', 'NETAPSYS',
# 'NOW CONSULTIANS GmbH & Co. KG', 'NWGG Pty Ltd', 'NY Foundling', 'Nara Syst Ltd.', 'Narwhals Consulting',
# 'Navarambh Software Pvt. Ltd.', 'Nearsoft Inc', 'Nemetschek Bulgaria', 'NetworkedAssets', 'New Media and
# Technologies Sp. z o.o.', 'New Relic', 'New Verve Consulting', 'Nextup.ai - Apps for Slack', 'Nimeko Software',
# 'NullPointerException Systems', 'Nuum Solutions', "O'Hara Group", 'OBSS', 'ONEPOINT Projects', 'OVD Group',
# 'Oboard', 'Okapya Software Solutions Inc.', 'Old Street Solutions', 'Oleg Burmistrov', 'Oliver Straesser',
# 'Oomnitza', 'Open Source Consulting', 'Optimizory Technologies Pvt. Ltd.', 'Orbitz', 'Ovyka', 'PMEase Inc',
# 'PagerDuty', 'Patrick Facheris', 'Patrik Varga', 'Pavel Baranchikov', 'Perfect Commit', 'Perforce Software',
# 'Petteri Kivimäki', 'Philipp Eckelmann', 'Pineant Plugins', 'Pirate Ninja Unicorn', 'Pitronote', 'Play SQL',
# 'Polar Shift Ltd.', 'Praecipio Software', 'Precision Plugins', 'Precog Software', 'Prepend', 'Prime Timesheet,
# s.r.o', 'Prism Project', 'ProductPlan', 'ProjectBalm', 'Projektron GmbH', 'ProtoShare / Astound Commerce',
# 'Purde Software', 'QMetry', 'Qameta Software', 'Qotilabs', 'Railsware', 'Ray Barham', 'Reconquest', 'Red Hat',
# 'Redmoon Software Ltd', 'Refined', 'Release Management', 'Reliex', 'Resight', 'Ricksoft, Inc.', 'Rixter AB',
# 'Ros Entertainment', 'Rozdoum', 'Rumpelcoders', 'SNG Technologies Ltd.', 'SPECTRUM GROUPE', 'STAGIL', 'Sandstorm',
# 'Sapling Valley', 'Sauce Labs', 'Schütze AG', 'Scolution GmbH & Co. KG', 'Sean Ford', 'SecSign Technologies',
# 'ServiceRocket', 'ServiceRocket Labs', 'Shanghai Digital Talent Technology Co., Ltd.', 'Shinetech Software',
# 'Shippable', 'Siemens AG, Corporate Technology', 'Sistel SL', 'Slie', 'Smadoa GmbH', 'SmartBear', 'SmartBear QAC',
# 'SmartDraw Software', 'SmartForce', 'Smateso - Smart Team Solutions', 'SoftComply', 'SoftCrts', 'SoftServe',
# 'Softlist', 'Software Quality Lab GmbH', 'SoftwarePlant', 'SolDevelo', 'Solveka', 'Sonatype', 'Sourcesense',
# 'Soyatec', 'Spartez Software', 'Sparx Systems Prolaborate', 'Steffen Stamprath', 'Stephan Bechter', 'StiltSoft',
# 'StiltSoft Labs', 'StonikByte', 'Strategery Solutions BVBA', 'StreamlineSoft', 'Structurizr', 'Sweet Bananas',
# 'Sylvain FRANCOIS', 'Sylvain LAURENT', 'Synack, Inc.', 'TEMPEST', 'TMate Software', 'TNG Technology Consulting
# GmbH', 'Taylor Jones', 'TeamSphere', 'TeamViewer GmbH', 'Teamlead', 'TechTime Initiative Group Limited', 'TechUp',
# 'Teemu Torvela', 'Tempo for JIRA', 'Test Collab', 'Test IT', 'The Crust Software', 'The Plugin People',
# 'The Starware', 'ThinkTilt', 'Tommer Lahat', 'ToolsPlus', 'Top Shelf Solutions', 'Toshihiro Sato', 'TouchDown',
# 'Transition Technologies PSC', 'Tricentis', 'Trimble Solutions Corporation', 'Ugubi.io', 'Unlimax', 'Utoolity',
# 'VINC Software', 'Valeriya Shevchenko', 'Veracode', 'Vertuna LLC', 'Vestmark', 'Vighnaharta', 'Viktor Kaydalov',
# 'Vilisoft', 'Vivid Inc.', 'W Knowledge', 'White Software', 'WhiteHat Security', 'WhiteSource', 'Wikistrat Inc.',
# 'Wim Deblauwe', 'Wittified Atlassian Apps (an Appfire company)', 'Wombats Corp', 'WorkBoard Inc.', 'Workfront
# Inc.', 'XALT Business Consulting GmbH', 'Xavier Arques', 'XebiaLabs', 'Xpand IT', 'YASSIN B', 'Yaroslav Lukyanov',
# 'Yiraphic', 'Young Plugins', 'Zendesk', 'acocon GmbH - business division greenique', 'airfocus GmbH', 'atSistemas',
# 'avono AG', 'beecom', 'bit2bit Americas', 'bitFit', 'bitvoodoo ag', 'bitvoodoo labs', 'buddybuild',
# 'catworkx GmbH', 'celix Solutions', 'codecentric AG', 'codeclou UG (haftungsbeschränkt)', 'codedoers',
# 'codefortynine GmbH', 'codescape - Stefan Glase', 'eMundo GmbH', 'eXtensi', 'ease solutions Pte Ltd', 'eazyBI',
# 'echocat', 'evolu software GmbH', 'excentia', 'flaregames GmbH', 'hasCode.com', 'hktxcn.com (汇科天下)', 'i0in.ltd',
# 'i4ware Software', 'iDalko', 'ij-solutions UG (haftungsbeschränkt)', 'ikuTeam', 'iorad inc.', 'it-economics GmbH',
# 'it.Lab Adam Labus', 'jPlugs', 'kyona GmbH', 'limon4ick', 'mgm technology partners', 'miniOrange', 'mirrorlake
# software', 'openmind', 'proventis GmbH', 'quisapps.com', 'resolution Reichert Network Solutions GmbH',
# 'ricebean.net', 'savignano software solutions', 'scmenthusiast', 'smartics', 'syracom AG', 't2consult', 'test IO',
# 'tibe.io GmbH', 'venITure', 'vendor_name', 'viadee Unternehmensberatung AG', 'view26 GmbH', 'wirecube',
# 'www.MrAddon.com ®', 'xMatters', 'yWorks GmbH', 'yasoon', 'zAgile', 'zenofx.com', 'Øystein Gisnås']
headers = {'Accept: application/json'}
non_top_vendors_list = []
non_top_vendors_details = {}
top_vendors_details = {}

print(len(vendor_list))
for vendor in vendor_list:
    base_url = 'https://marketplace.atlassian.com/rest/2/vendors'
    url = '?text='.join([base_url, vendor])
    # print (url)
    print('Vendor: ', vendor)
    r = requests.get(url)
    r_json = json.loads(r.text)
    # print (r_json)
    # print ('Count:' ,r_json['count'])
    if r_json['count'] != 0:
        # print (len(r_json['_embedded']['vendors']))
        for n in range(0, len(r_json['_embedded']['vendors'])):
            print('Vendor name from response:', r_json['_embedded']['vendors'][n]['name'])
            # print ('Vendor id from response: ',r_json['_embedded']['vendors'][n]['_links']['self']['href'][16:])
            if r_json['_embedded']['vendors'][n]['programs']:
                # print (r_json['_embedded']['vendors'][n]['programs'])
                top_vendors_details[(r_json['_embedded']['vendors'][n]['name'])] = [
                    r_json['_embedded']['vendors'][n]['_links']['self']['href'][16:]]
            else:
                print('Not a top vendor')
                non_top_vendors_list.append(r_json['_embedded']['vendors'][n]['name'])
                non_top_vendors_details[(r_json['_embedded']['vendors'][n]['name'])] = [
                    r_json['_embedded']['vendors'][n]['_links']['self']['href'][16:]]
    else:
        print('No such vendor found')
    # print (non_top_vendors_list)
    # print (r_json['_embedded']['vendors'][0]['programs'])
    # print ('Vendor name from response:', r_json['_embedded']['vendors'][0]['name'])
print('Non Top Vendor Details', non_top_vendors_details)
print('Nu of Non Top Vendors in the list', len(non_top_vendors_details))
print('Top Vendor Details', top_vendors_details)
print('Nu of Top Vendor Details', len(top_vendors_details))

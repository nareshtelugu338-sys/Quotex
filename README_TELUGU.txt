QUOTEX SIGNAL PWA — తెలుగు సెటప్

ముఖ్యమైన విషయాలు
- Quotex అధికారిక API లేదు. ఇది OTCharts అనే third-party read-only market-data serviceను ఉపయోగిస్తుంది.
- ఈ package ఏ trade/orderను place చేయదు.
- API keyను HTML/JavaScriptలో పెట్టకండి. Backend server environmentలో మాత్రమే ఉంచండి.
- OTCharts free keyలో live streaming ఉండకపోవచ్చు; live data/plan access మరియు quota మీ accountపై ఆధారపడతాయి.
- PWA install కోసం HTTPS hosting అవసరం (localhost మినహా). ఈ package deploy చేయడానికి సిద్ధంగా ఉంది; public hosting మీరు configure చేయాలి.

LOCAL TEST (కంప్యూటర్‌లో)
1. Python 3 ఉన్న కంప్యూటర్‌లో ZIP extract చేయండి.
2. OTCharts accountలో మీ keyకి Quotex book access ఉందని నిర్ధారించండి.
3. Windows PowerShell తెరిచి project folderకి వెళ్లండి.
4. PowerShellలో:
   $env:OTCHARTS_API_KEY="మీ_KEY_ఇక్కడ"
   python app.py
5. అదే కంప్యూటర్‌లో http://127.0.0.1:8000 తెరవండి.
6. Androidలో అదే Wi-Fiలో ఉంటే PC యొక్క local IPతో http://PC-IP:8000 తెరవవచ్చు. అయితే HTTP LAN addressపై PWA install option browser/device బట్టి అందుబాటులో ఉండకపోవచ్చు.

ANDROIDలో INSTALLABLE PWA
1. HTTPS ఉన్న Python hosting/serverకు ఈ project deploy చేయాలి.
2. Hosting dashboardలో secret/environment variable OTCHARTS_API_KEY సెట్ చేయండి. Keyను source codeలో commit చేయవద్దు.
3. Hosting provider start command: python app.py
4. HTTPS URL Android Chromeలో తెరవండి.
5. Chrome menu (⋮) > Install app లేదా Add to Home screen నొక్కండి.

వాడే విధానం
1. Instruments లోడ్ చేయండి.
2. OTC మాత్రమే / Normal మాత్రమే / అన్ని instruments ఎంచుకోండి.
3. instrument, M1 లేదా M5 ఎంచుకోండి.
4. “Candles తీసుకొని Signal విశ్లేషించండి” నొక్కండి.
5. BUY/SELL/NO TRADE ఫలితాన్ని చూడండి.
6. కొత్త విశ్లేషణ కావాలంటే బటన్‌ను మళ్లీ నొక్కండి. ఇది నిరంతరం polling చేయదు.

సిగ్నల్ నియమాలు
BUY: EMA9 > EMA21 మరియు RSI 50–70
SELL: EMA9 < EMA21 మరియు RSI 30–50
లేకపోతే NO TRADE
Data gaps ఉంటే NO TRADE చూపిస్తుంది. ఇవి demonstration rules మాత్రమే; profitability లేదా accuracy హామీ లేదు.

సమస్య పరిష్కారం
- 401/403: key తప్పు కావచ్చు లేదా Quotex book అనుమతి/plan లేదు.
- quota error: OTCharts usage చూడండి; పదేపదే request చేయవద్దు.
- live data అందకపోతే: మీ key/planకు streaming లేదా కావలసిన instrument access ఉందో పరిశీలించండి.
- symbol list ఖాళీ అయితే: API access, key మరియు network తనిఖీ చేయండి.

గమనిక: Android PWA installabilityకి HTTPS అవసరం. Backendను internetలో deploy చేస్తే API key secret environment variableలో ఉంచండి; public repoలో key ఎప్పుడూ పెట్టకండి.

{
    "type": "MySQLNotebook",
    "version": "1.0",
    "caption": "Script",
    "content": "# creare utente\nCREATE USER `user`@localhost IDENTIFIED BY 'password';\nCREATE USER its2026@localhost IDENTIFIED BY 'password';\n\n# creare database\nCREATE DATABASE provamicrofono;\nCREATE DATABASE its2026;\n\n# assegnare permessi a utente su database\nGRANT ALL on provamicrofono.* TO user@localhost;\nGRANT ALL on its2026.* TO its2026@localhost;\n\n# connessione da utente a database\n# mysql -u user -p\n\n# creazione di tabella\nCREATE TABLE provamicrofono.citta LIKE world.city;\n\n# inserimento / lettura / modifica  / eliminazione record\nINSERT INTO provamicrofono.citta \nSELECT * from world.city;\n\nSELECT * FROM provamicrofono.citta;\nSELECT DISTINCT CountryCode from provamicrofono.citta;\nSELECT * FROM provamicrofono.citta WHERE CountryCode = 'ITA';\nSELECT * FROM provamicrofono.citta WHERE CountryCode = 'ITA' and District = 'Apulia';\nSELECT CountryCode , SUM(population) AS abitanti \nfrom provamicrofono.citta \ngroup by countrycode\norder by CountryCode asc;\n\n# eliminazione tabella\n\n\n# revocare privilegi\n\n\n# eliminare database\n\n\n# eliminare utente\n\n",
    "options": {
        "tabSize": 4,
        "insertSpaces": true,
        "indentSize": 4,
        "defaultEOL": "CRLF",
        "trimAutoWhitespace": true
    },
    "viewState": null,
    "contexts": [
        {
            "state": {
                "start": 1,
                "end": 43,
                "language": "mysql",
                "result": {
                    "type": "resultIds",
                    "list": [
                        "94354f9e-77e5-410d-d0c1-a2a3a223b939"
                    ]
                },
                "currentHeight": 207.77774047851562,
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 70
                        },
                        "contentStart": 16,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 70,
                            "length": 56
                        },
                        "contentStart": 71,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 126,
                            "length": 51
                        },
                        "contentStart": 146,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 177,
                            "length": 25
                        },
                        "contentStart": 178,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 202,
                            "length": 92
                        },
                        "contentStart": 246,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 294,
                            "length": 45
                        },
                        "contentStart": 295,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 339,
                            "length": 130
                        },
                        "contentStart": 419,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 469,
                            "length": 119
                        },
                        "contentStart": 529,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 588,
                            "length": 37
                        },
                        "contentStart": 590,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 625,
                            "length": 55
                        },
                        "contentStart": 626,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 680,
                            "length": 62
                        },
                        "contentStart": 681,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 742,
                            "length": 86
                        },
                        "contentStart": 743,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 828,
                            "length": 124
                        },
                        "contentStart": 829,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 952,
                            "length": 93
                        },
                        "contentStart": 951,
                        "state": 3
                    }
                ]
            },
            "data": [
                {
                    "tabId": "60129cfb-b083-4347-bb57-0bfd2f342187",
                    "resultId": "94354f9e-77e5-410d-d0c1-a2a3a223b939",
                    "rows": [
                        {
                            "0": "CHN",
                            "1": "175953614"
                        },
                        {
                            "0": "IND",
                            "1": "123298526"
                        },
                        {
                            "0": "BRA",
                            "1": "85876862"
                        },
                        {
                            "0": "USA",
                            "1": "78625774"
                        },
                        {
                            "0": "JPN",
                            "1": "77965107"
                        },
                        {
                            "0": "RUS",
                            "1": "69150700"
                        },
                        {
                            "0": "MEX",
                            "1": "59752521"
                        },
                        {
                            "0": "KOR",
                            "1": "38999893"
                        },
                        {
                            "0": "IDN",
                            "1": "37485695"
                        },
                        {
                            "0": "PAK",
                            "1": "31546745"
                        },
                        {
                            "0": "PHL",
                            "1": "30934791"
                        },
                        {
                            "0": "TUR",
                            "1": "28327028"
                        },
                        {
                            "0": "DEU",
                            "1": "26245483"
                        },
                        {
                            "0": "IRN",
                            "1": "26032990"
                        },
                        {
                            "0": "GBR",
                            "1": "22436673"
                        },
                        {
                            "0": "COL",
                            "1": "20250990"
                        },
                        {
                            "0": "EGY",
                            "1": "20083079"
                        },
                        {
                            "0": "UKR",
                            "1": "20074000"
                        },
                        {
                            "0": "ARG",
                            "1": "19996563"
                        },
                        {
                            "0": "NGA",
                            "1": "17366900"
                        },
                        {
                            "0": "ESP",
                            "1": "16669189"
                        },
                        {
                            "0": "ZAF",
                            "1": "15196370"
                        },
                        {
                            "0": "ITA",
                            "1": "15087019"
                        },
                        {
                            "0": "TWN",
                            "1": "13569336"
                        },
                        {
                            "0": "CAN",
                            "1": "12673840"
                        },
                        {
                            "0": "VEN",
                            "1": "12251091"
                        },
                        {
                            "0": "PER",
                            "1": "12147242"
                        },
                        {
                            "0": "POL",
                            "1": "11687431"
                        },
                        {
                            "0": "AUS",
                            "1": "11313666"
                        },
                        {
                            "0": "SAU",
                            "1": "10636700"
                        },
                        {
                            "0": "COD",
                            "1": "9864615"
                        },
                        {
                            "0": "CHL",
                            "1": "9717970"
                        },
                        {
                            "0": "VNM",
                            "1": "9364813"
                        },
                        {
                            "0": "FRA",
                            "1": "9244494"
                        },
                        {
                            "0": "IRQ",
                            "1": "8926041"
                        },
                        {
                            "0": "MAR",
                            "1": "8757562"
                        },
                        {
                            "0": "BGD",
                            "1": "8569906"
                        },
                        {
                            "0": "THA",
                            "1": "7953161"
                        },
                        {
                            "0": "ROM",
                            "1": "7469006"
                        },
                        {
                            "0": "PRK",
                            "1": "6476751"
                        },
                        {
                            "0": "MMR",
                            "1": "6203000"
                        },
                        {
                            "0": "ECU",
                            "1": "5744142"
                        },
                        {
                            "0": "KAZ",
                            "1": "5484200"
                        },
                        {
                            "0": "DZA",
                            "1": "5192179"
                        },
                        {
                            "0": "UZB",
                            "1": "5183900"
                        },
                        {
                            "0": "NLD",
                            "1": "5180049"
                        },
                        {
                            "0": "SDN",
                            "1": "4752187"
                        },
                        {
                            "0": "BLR",
                            "1": "4741000"
                        },
                        {
                            "0": "CUB",
                            "1": "4629925"
                        },
                        {
                            "0": "MYS",
                            "1": "4605141"
                        },
                        {
                            "0": "SYR",
                            "1": "4477784"
                        },
                        {
                            "0": "SGP",
                            "1": "4017733"
                        },
                        {
                            "0": "KEN",
                            "1": "3522793"
                        },
                        {
                            "0": "CMR",
                            "1": "3522554"
                        },
                        {
                            "0": "BOL",
                            "1": "3378644"
                        },
                        {
                            "0": "HKG",
                            "1": "3300633"
                        },
                        {
                            "0": "CIV",
                            "1": "3191137"
                        },
                        {
                            "0": "ETH",
                            "1": "3190334"
                        },
                        {
                            "0": "MOZ",
                            "1": "3143145"
                        },
                        {
                            "0": "HUN",
                            "1": "2953310"
                        },
                        {
                            "0": "TZA",
                            "1": "2944034"
                        },
                        {
                            "0": "SWE",
                            "1": "2891431"
                        },
                        {
                            "0": "ISR",
                            "1": "2813000"
                        },
                        {
                            "0": "SEN",
                            "1": "2770458"
                        },
                        {
                            "0": "ZWE",
                            "1": "2730420"
                        },
                        {
                            "0": "LBY",
                            "1": "2697007"
                        },
                        {
                            "0": "BGR",
                            "1": "2696915"
                        },
                        {
                            "0": "CZE",
                            "1": "2634711"
                        },
                        {
                            "0": "AGO",
                            "1": "2561600"
                        },
                        {
                            "0": "ZMB",
                            "1": "2473500"
                        },
                        {
                            "0": "AZE",
                            "1": "2464000"
                        },
                        {
                            "0": "DOM",
                            "1": "2438276"
                        },
                        {
                            "0": "AUT",
                            "1": "2384273"
                        },
                        {
                            "0": "AFG",
                            "1": "2332100"
                        },
                        {
                            "0": "YUG",
                            "1": "2189507"
                        },
                        {
                            "0": "GRC",
                            "1": "1972843"
                        },
                        {
                            "0": "GEO",
                            "1": "1880900"
                        },
                        {
                            "0": "JOR",
                            "1": "1847677"
                        },
                        {
                            "0": "NZL",
                            "1": "1847600"
                        },
                        {
                            "0": "GHA",
                            "1": "1819889"
                        },
                        {
                            "0": "TUN",
                            "1": "1798500"
                        },
                        {
                            "0": "YEM",
                            "1": "1743700"
                        },
                        {
                            "0": "ARE",
                            "1": "1728336"
                        },
                        {
                            "0": "ARM",
                            "1": "1633100"
                        },
                        {
                            "0": "BEL",
                            "1": "1609322"
                        },
                        {
                            "0": "PRI",
                            "1": "1564174"
                        },
                        {
                            "0": "LKA",
                            "1": "1545000"
                        },
                        {
                            "0": "FIN",
                            "1": "1532919"
                        },
                        {
                            "0": "HTI",
                            "1": "1517338"
                        },
                        {
                            "0": "LTU",
                            "1": "1473317"
                        },
                        {
                            "0": "COG",
                            "1": "1450000"
                        },
                        {
                            "0": "LBN",
                            "1": "1340000"
                        },
                        {
                            "0": "HND",
                            "1": "1287000"
                        },
                        {
                            "0": "NIC",
                            "1": "1269223"
                        },
                        {
                            "0": "URY",
                            "1": "1236000"
                        },
                        {
                            "0": "BFA",
                            "1": "1229000"
                        },
                        {
                            "0": "GTM",
                            "1": "1225188"
                        },
                        {
                            "0": "DNK",
                            "1": "1215945"
                        },
                        {
                            "0": "MDA",
                            "1": "1193300"
                        },
                        {
                            "0": "SOM",
                            "1": "1177000"
                        },
                        {
                            "0": "HRV",
                            "1": "1168883"
                        },
                        {
                            "0": "PRT",
                            "1": "1145011"
                        },
                        {
                            "0": "SLV",
                            "1": "1138231"
                        },
                        {
                            "0": "NPL",
                            "1": "1132403"
                        },
                        {
                            "0": "MDG",
                            "1": "1123161"
                        },
                        {
                            "0": "NOR",
                            "1": "1100028"
                        },
                        {
                            "0": "GIN",
                            "1": "1090610"
                        },
                        {
                            "0": "PRY",
                            "1": "1020020"
                        },
                        {
                            "0": "TKM",
                            "1": "972600"
                        },
                        {
                            "0": "LVA",
                            "1": "968596"
                        },
                        {
                            "0": "BEN",
                            "1": "968503"
                        },
                        {
                            "0": "CHE",
                            "1": "914200"
                        },
                        {
                            "0": "MWI",
                            "1": "914119"
                        },
                        {
                            "0": "PSE",
                            "1": "902360"
                        },
                        {
                            "0": "UGA",
                            "1": "890800"
                        },
                        {
                            "0": "LBR",
                            "1": "850000"
                        },
                        {
                            "0": "SLE",
                            "1": "850000"
                        },
                        {
                            "0": "KGZ",
                            "1": "812100"
                        },
                        {
                            "0": "MLI",
                            "1": "809552"
                        },
                        {
                            "0": "KHM",
                            "1": "805055"
                        },
                        {
                            "0": "PAN",
                            "1": "786755"
                        },
                        {
                            "0": "SVK",
                            "1": "784143"
                        },
                        {
                            "0": "MNG",
                            "1": "773700"
                        },
                        {
                            "0": "MRT",
                            "1": "764900"
                        },
                        {
                            "0": "TJK",
                            "1": "685500"
                        },
                        {
                            "0": "NER",
                            "1": "653857"
                        },
                        {
                            "0": "TCD",
                            "1": "630465"
                        },
                        {
                            "0": "LAO",
                            "1": "628452"
                        },
                        {
                            "0": "IRL",
                            "1": "609041"
                        },
                        {
                            "0": "BIH",
                            "1": "599106"
                        },
                        {
                            "0": "OMN",
                            "1": "537096"
                        },
                        {
                            "0": "CAF",
                            "1": "524000"
                        },
                        {
                            "0": "EST",
                            "1": "505227"
                        },
                        {
                            "0": "MKD",
                            "1": "444299"
                        },
                        {
                            "0": "MAC",
                            "1": "437500"
                        },
                        {
                            "0": "ERI",
                            "1": "431000"
                        },
                        {
                            "0": "GAB",
                            "1": "419000"
                        },
                        {
                            "0": "SVN",
                            "1": "386518"
                        },
                        {
                            "0": "DJI",
                            "1": "383000"
                        },
                        {
                            "0": "TGO",
                            "1": "375000"
                        },
                        {
                            "0": "QAT",
                            "1": "355000"
                        },
                        {
                            "0": "CYP",
                            "1": "349400"
                        },
                        {
                            "0": "CRI",
                            "1": "339131"
                        },
                        {
                            "0": "MUS",
                            "1": "337280"
                        },
                        {
                            "0": "BWA",
                            "1": "314822"
                        },
                        {
                            "0": "JAM",
                            "1": "314140"
                        },
                        {
                            "0": "BDI",
                            "1": "300000"
                        },
                        {
                            "0": "LSO",
                            "1": "297000"
                        },
                        {
                            "0": "RWA",
                            "1": "286000"
                        },
                        {
                            "0": "ALB",
                            "1": "270000"
                        },
                        {
                            "0": "KWT",
                            "1": "261252"
                        },
                        {
                            "0": "GUY",
                            "1": "254000"
                        },
                        {
                            "0": "PNG",
                            "1": "247000"
                        },
                        {
                            "0": "GNB",
                            "1": "241000"
                        },
                        {
                            "0": "BHS",
                            "1": "172000"
                        },
                        {
                            "0": "ESH",
                            "1": "169000"
                        },
                        {
                            "0": "NAM",
                            "1": "169000"
                        },
                        {
                            "0": "BHR",
                            "1": "148000"
                        },
                        {
                            "0": "GMB",
                            "1": "144926"
                        },
                        {
                            "0": "REU",
                            "1": "131480"
                        },
                        {
                            "0": "SUR",
                            "1": "112000"
                        },
                        {
                            "0": "ISL",
                            "1": "109184"
                        },
                        {
                            "0": "TTO",
                            "1": "99997"
                        },
                        {
                            "0": "CPV",
                            "1": "94800"
                        },
                        {
                            "0": "MTQ",
                            "1": "94050"
                        },
                        {
                            "0": "LUX",
                            "1": "80700"
                        },
                        {
                            "0": "FJI",
                            "1": "77366"
                        },
                        {
                            "0": "NCL",
                            "1": "76293"
                        },
                        {
                            "0": "GLP",
                            "1": "75380"
                        },
                        {
                            "0": "MDV",
                            "1": "71000"
                        },
                        {
                            "0": "BLZ",
                            "1": "62915"
                        },
                        {
                            "0": "SWZ",
                            "1": "61000"
                        },
                        {
                            "0": "PYF",
                            "1": "51441"
                        },
                        {
                            "0": "GUF",
                            "1": "50699"
                        },
                        {
                            "0": "SLB",
                            "1": "50100"
                        },
                        {
                            "0": "STP",
                            "1": "49541"
                        },
                        {
                            "0": "TMP",
                            "1": "47900"
                        },
                        {
                            "0": "SYC",
                            "1": "41000"
                        },
                        {
                            "0": "GNQ",
                            "1": "40000"
                        },
                        {
                            "0": "COM",
                            "1": "36000"
                        },
                        {
                            "0": "WSM",
                            "1": "35900"
                        },
                        {
                            "0": "VUT",
                            "1": "33700"
                        },
                        {
                            "0": "FSM",
                            "1": "30600"
                        },
                        {
                            "0": "ABW",
                            "1": "29034"
                        },
                        {
                            "0": "MLT",
                            "1": "28518"
                        },
                        {
                            "0": "MHL",
                            "1": "28000"
                        },
                        {
                            "0": "GIB",
                            "1": "27025"
                        },
                        {
                            "0": "ATG",
                            "1": "24000"
                        },
                        {
                            "0": "TON",
                            "1": "22400"
                        },
                        {
                            "0": "BTN",
                            "1": "22000"
                        },
                        {
                            "0": "BRN",
                            "1": "21484"
                        },
                        {
                            "0": "AND",
                            "1": "21189"
                        },
                        {
                            "0": "CYM",
                            "1": "19600"
                        },
                        {
                            "0": "VCT",
                            "1": "17100"
                        },
                        {
                            "0": "DMA",
                            "1": "16243"
                        },
                        {
                            "0": "FRO",
                            "1": "14542"
                        },
                        {
                            "0": "MCO",
                            "1": "14388"
                        },
                        {
                            "0": "GRL",
                            "1": "13445"
                        },
                        {
                            "0": "VIR",
                            "1": "13000"
                        },
                        {
                            "0": "MYT",
                            "1": "12000"
                        },
                        {
                            "0": "PLW",
                            "1": "12000"
                        },
                        {
                            "0": "COK",
                            "1": "11900"
                        },
                        {
                            "0": "KNA",
                            "1": "11600"
                        },
                        {
                            "0": "GUM",
                            "1": "10639"
                        },
                        {
                            "0": "LIE",
                            "1": "10389"
                        },
                        {
                            "0": "MNP",
                            "1": "9200"
                        },
                        {
                            "0": "VGB",
                            "1": "8000"
                        },
                        {
                            "0": "ASM",
                            "1": "7523"
                        },
                        {
                            "0": "KIR",
                            "1": "7281"
                        },
                        {
                            "0": "SMR",
                            "1": "7096"
                        },
                        {
                            "0": "BRB",
                            "1": "6070"
                        },
                        {
                            "0": "SPM",
                            "1": "5808"
                        },
                        {
                            "0": "TCA",
                            "1": "4800"
                        },
                        {
                            "0": "GRD",
                            "1": "4621"
                        },
                        {
                            "0": "NRU",
                            "1": "4609"
                        },
                        {
                            "0": "TUV",
                            "1": "4600"
                        },
                        {
                            "0": "BMU",
                            "1": "3000"
                        },
                        {
                            "0": "ANT",
                            "1": "2345"
                        },
                        {
                            "0": "LCA",
                            "1": "2301"
                        },
                        {
                            "0": "MSR",
                            "1": "2000"
                        },
                        {
                            "0": "FLK",
                            "1": "1636"
                        },
                        {
                            "0": "AIA",
                            "1": "1556"
                        },
                        {
                            "0": "SHN",
                            "1": "1500"
                        },
                        {
                            "0": "SJM",
                            "1": "1438"
                        },
                        {
                            "0": "WLF",
                            "1": "1137"
                        },
                        {
                            "0": "NFK",
                            "1": "800"
                        },
                        {
                            "0": "CXR",
                            "1": "700"
                        },
                        {
                            "0": "NIU",
                            "1": "682"
                        },
                        {
                            "0": "CCK",
                            "1": "670"
                        },
                        {
                            "0": "VAT",
                            "1": "455"
                        },
                        {
                            "0": "TKL",
                            "1": "300"
                        },
                        {
                            "0": "PCN",
                            "1": "42"
                        }
                    ],
                    "columns": [
                        {
                            "title": "CountryCode",
                            "field": "0",
                            "dataType": {
                                "type": 17,
                                "characterMaximumLength": 65535,
                                "flags": [
                                    "BINARY",
                                    "ASCII",
                                    "UNICODE"
                                ],
                                "needsQuotes": true,
                                "parameterFormatType": "OneOrZero"
                            },
                            "inPK": false,
                            "nullable": false,
                            "autoIncrement": false
                        },
                        {
                            "title": "abitanti",
                            "field": "1",
                            "dataType": {
                                "type": 10,
                                "flags": [
                                    "UNSIGNED",
                                    "ZEROFILL"
                                ],
                                "numericPrecision": 65,
                                "numericScale": 30,
                                "parameterFormatType": "TwoOrOneOrZero",
                                "synonyms": [
                                    "FIXED",
                                    "NUMERIC",
                                    "DEC"
                                ]
                            },
                            "inPK": false,
                            "nullable": false,
                            "autoIncrement": false
                        }
                    ],
                    "executionInfo": {
                        "text": "OK, 232 records retrieved in 9.558ms"
                    },
                    "totalRowCount": 232,
                    "hasMoreRows": false,
                    "currentPage": 0,
                    "index": 0,
                    "sql": "\nSELECT CountryCode , SUM(population) AS abitanti \nfrom provamicrofono.citta \ngroup by countrycode\norder by abitanti desc;",
                    "updatable": false,
                    "fullTableName": ""
                }
            ]
        },
        {
            "state": {
                "start": 1,
                "end": 43,
                "language": "mysql",
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 68
                        },
                        "contentStart": 16,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 68,
                            "length": 279
                        },
                        "contentStart": 67,
                        "state": 3
                    }
                ]
            },
            "data": []
        }
    ]
}
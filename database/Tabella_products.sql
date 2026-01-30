{
    "type": "MySQLNotebook",
    "version": "1.0",
    "caption": "Script",
    "content": "# ISTRUZIONI DDL\n\nUSE its2026;\n\nCREATE TABLE IF NOT EXISTS products (\n    product_id INT PRIMARY KEY AUTO_INCREMENT,\n    name varchar(30) NOT NULL,\n    price decimal(6,2) NOT NULL DEFAULT 0.0,\n    category ENUM('abbigliamento', 'casalinghi')\n);\n\nALTER TABLE products\nADD COLUMN price_after_vat DECIMAL(6,2) NOT NULL DEFAULT 0.0;\n\nDESCRIBE products;\n\n# CRUD su database\n\n# C: CREATE (INSERT)\nINSERT INTO products \nVALUE \n(NULL, 'Maglia Verde', DEFAULT, 'abbigliamento');\n\nINSERT INTO products \nVALUES \n(NULL, 'Maglia Gialla', DEFAULT, 'abbigliamento'),\n(NULL, 'Maglia Rossa', 10, 'abbigliamento');\n\nINSERT INTO products (`name`, price, category)\nVALUES\n('Maglia Blu', 10, 'abbigliamento');\n\n\nINSERT INTO products (category, `name`)\nVALUES\n('abbigliamento', 'Maglia Bucata');\n\n# R: READ - RETRIEVE (SELECT)\nSELECT * FROM \nproducts;\n\nSELECT name as Nome, price as Prezzo FROM \nproducts;\n\nSELECT name as Nome, price as Prezzo FROM \nproducts\nORDER BY Prezzo desc, Nome;\n\n# U: UPDATE (update)\nUPDATE products \nSET \nprice = 5.5\nWHERE\nprice = 0.0;\n\nUPDATE products \nSET \nprice_after_vat = price * 1.22;\n\n# D: DELETE (delete)\nDELETE FROM products\nWHERE product_id = 5;\n\nDELETE FROM products\nWHERE name = 'Maglia Bucata';\n\nDELETE FROM products\nWHERE name LIKE '%Gialla%';\n\n\n\n",
    "options": {
        "tabSize": 4,
        "indentSize": 4,
        "insertSpaces": true,
        "defaultEOL": "LF",
        "trimAutoWhitespace": true
    },
    "viewState": null,
    "contexts": [
        {
            "state": {
                "start": 1,
                "end": 72,
                "language": "mysql",
                "result": {
                    "type": "resultIds",
                    "list": [
                        "6f5a56f9-d3d7-4a42-f1d0-4dbf8becc52e"
                    ]
                },
                "currentHeight": 200,
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 30
                        },
                        "contentStart": 18,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 30,
                            "length": 214
                        },
                        "contentStart": 32,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 244,
                            "length": 84
                        },
                        "contentStart": 246,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 328,
                            "length": 20
                        },
                        "contentStart": 331,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 348,
                            "length": 121
                        },
                        "contentStart": 391,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 469,
                            "length": 127
                        },
                        "contentStart": 471,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 596,
                            "length": 92
                        },
                        "contentStart": 598,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 688,
                            "length": 85
                        },
                        "contentStart": 691,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 773,
                            "length": 2
                        },
                        "contentStart": 772,
                        "state": 3
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 773,
                            "length": 56
                        },
                        "contentStart": 805,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 829,
                            "length": 54
                        },
                        "contentStart": 831,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 883,
                            "length": 81
                        },
                        "contentStart": 885,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 964,
                            "length": 75
                        },
                        "contentStart": 987,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1039,
                            "length": 55
                        },
                        "contentStart": 1041,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1094,
                            "length": 65
                        },
                        "contentStart": 1118,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1159,
                            "length": 52
                        },
                        "contentStart": 1162,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1211,
                            "length": 50
                        },
                        "contentStart": 1214,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 1261,
                            "length": 4
                        },
                        "contentStart": 1260,
                        "state": 3
                    }
                ]
            },
            "data": [
                {
                    "tabId": "f5e8fcf2-867e-4216-d1d3-29600191ac74",
                    "resultId": "6f5a56f9-d3d7-4a42-f1d0-4dbf8becc52e",
                    "rows": [
                        {
                            "0": "Maglia Blu",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Blu",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Rossa",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Rossa",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Verde",
                            "1": "5.50"
                        },
                        {
                            "0": "Maglia Verde",
                            "1": "5.50"
                        }
                    ],
                    "columns": [
                        {
                            "title": "Nome",
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
                            "title": "Prezzo",
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
                        "text": "OK, 6 records retrieved in 0.74ms"
                    },
                    "totalRowCount": 6,
                    "hasMoreRows": false,
                    "currentPage": 0,
                    "index": 0,
                    "sql": "\n\nSELECT name as Nome, price as Prezzo FROM \nproducts\nORDER BY Prezzo desc, Nome;",
                    "updatable": false,
                    "fullTableName": "products"
                }
            ]
        },
        {
            "state": {
                "start": 1,
                "end": 72,
                "language": "mysql",
                "currentSet": 1,
                "statements": [
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 0,
                            "length": 12
                        },
                        "contentStart": 0,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 12,
                            "length": 214
                        },
                        "contentStart": 14,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 226,
                            "length": 20
                        },
                        "contentStart": 229,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 246,
                            "length": 120
                        },
                        "contentStart": 288,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 366,
                            "length": 127
                        },
                        "contentStart": 368,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 493,
                            "length": 92
                        },
                        "contentStart": 495,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 585,
                            "length": 85
                        },
                        "contentStart": 588,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 670,
                            "length": 47
                        },
                        "contentStart": 693,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 717,
                            "length": 36
                        },
                        "contentStart": 719,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 753,
                            "length": 4
                        },
                        "contentStart": 752,
                        "state": 3
                    }
                ]
            },
            "data": []
        }
    ]
}
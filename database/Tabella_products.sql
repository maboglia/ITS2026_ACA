{
    "type": "MySQLNotebook",
    "version": "1.0",
    "caption": "Script",
    "content": "USE its2026;\n\nCREATE TABLE IF NOT EXISTS products (\n    product_id INT PRIMARY KEY AUTO_INCREMENT,\n    name varchar(30) NOT NULL,\n    price decimal(6,2) NOT NULL DEFAULT 0.0,\n    category ENUM('abbigliamento', 'casalinghi')\n);\n\nDESCRIBE products;\n\n# CRUD su database\n\n# C CREATE (INSERT)\nINSERT INTO products \nVALUE \n(NULL, 'Maglia Verde', DEFAULT, 'abbigliamento');\n\nINSERT INTO products \nVALUES \n(NULL, 'Maglia Gialla', DEFAULT, 'abbigliamento'),\n(NULL, 'Maglia Rossa', 10, 'abbigliamento');\n\nINSERT INTO products (`name`, price, category)\nVALUES\n('Maglia Blu', 10, 'abbigliamento');\n\n\nINSERT INTO products (category, `name`)\nVALUES\n('abbigliamento', 'Maglia Bucata');\n\n# R: READ - RETRIEVE\nSELECT * FROM \nproducts;\n\nSELECT name as Nome, price as Prezzo FROM \nproducts;\n\n\n\n",
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
                "end": 42,
                "language": "mysql",
                "result": {
                    "type": "resultIds",
                    "list": [
                        "86a100a5-937c-45d7-d172-181e0ade5ec0"
                    ]
                },
                "currentHeight": 300,
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
                            "length": 2
                        },
                        "contentStart": 669,
                        "state": 3
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
                            "length": 54
                        },
                        "contentStart": 719,
                        "state": 0
                    },
                    {
                        "delimiter": ";",
                        "span": {
                            "start": 771,
                            "length": 4
                        },
                        "contentStart": 770,
                        "state": 3
                    }
                ]
            },
            "data": [
                {
                    "tabId": "f5e8fcf2-867e-4216-d1d3-29600191ac74",
                    "resultId": "86a100a5-937c-45d7-d172-181e0ade5ec0",
                    "rows": [
                        {
                            "0": "Maglia Verde",
                            "1": "0.00"
                        },
                        {
                            "0": "Maglia Gialla",
                            "1": "0.00"
                        },
                        {
                            "0": "Maglia Rossa",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Blu",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Bucata",
                            "1": "0.00"
                        },
                        {
                            "0": "Maglia Verde",
                            "1": "0.00"
                        },
                        {
                            "0": "Maglia Gialla",
                            "1": "0.00"
                        },
                        {
                            "0": "Maglia Rossa",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Blu",
                            "1": "10.00"
                        },
                        {
                            "0": "Maglia Bucata",
                            "1": "0.00"
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
                        "text": "OK, 10 records retrieved in 0.63ms"
                    },
                    "totalRowCount": 10,
                    "hasMoreRows": false,
                    "currentPage": 0,
                    "index": 0,
                    "sql": "\n\nSELECT name as Nome, price as Prezzo FROM \nproducts;",
                    "updatable": false,
                    "fullTableName": "products"
                }
            ]
        },
        {
            "state": {
                "start": 1,
                "end": 42,
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
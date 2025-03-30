{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Generar analizador léxico",
            "type": "shell",
            "command": "flex",
            "args": ["${file}"],
            "problemMatcher": [],
            "group": {
                "kind": "build",
                "isDefault": true
            }
        },
        {
            "label": "Compilar analizador léxico",
            "type": "shell",
            "command": "gcc",
            "args": ["lex.yy.c", "-o", "${fileBasenameNoExtension}.exe", "-lfl"],
            "problemMatcher": [],
            "dependsOn": ["Generar analizador léxico"]
        }
    ]
}
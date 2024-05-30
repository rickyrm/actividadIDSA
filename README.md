# Configurar Git globalmente
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@example.com"
```

# Inicializar repositorio local
```bash
cd /ruta/a/tu/proyecto
git init
```

# Agregar archivos y hacer commit inicial
```bash
git add .
git commit -m "Initial commit with calculator implementation and tests"
```

# Crear repositorio en GitHub y obtener la URL (reemplaza con tu URL)
```bash
git remote add origin https://github.com/tu-usuario/simple-calculator.git
```
# Cambiar el nombre de la rama principal a main (opcional pero recomendable)
```bash
git branch -M main
```

# Enviar el commit inicial al repositorio remoto
```bash
git push -u origin main
```

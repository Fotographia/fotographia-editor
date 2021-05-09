# Notes

## requirements.txt
Σε αυτό το αρχείο είναι δηλωμένες όλες οι βιβλιοθήκες

## docker-compose.yml, Dockerfile
Αρχεία που χρειάζεται για να τρέξει το Docker. Άν δεν χρησιμοποιείτε docker αγνοήστε τα

## fotographia.toml .vscode .pre-commit-config.yaml .flake8
Αρχεία που είναι configured το black. Είναι για να γίνεται lint ο κώδικας και να είναι καθαρός

### app.py
Αυτό το αρχείο αποτελεί την εφαρμογή

### utils
Σε αυτό το φάκελο θα μπαίνουν όλες οι functions που έχουν να κάνουν 
με την επεξεργασία εικονών καθώς και διάφορες helper functions που
πιθανόν να χρειαστόυμε. π.χ.

```python
def resize(image)
    resized_image = blahblahblah()
    return resized_image
```

Ο σκοπός είναι να τις κάνουμε import στον φάκελο views και να τις 
χρησιμοποιούμε στο REST API.

### views (coming soon)
Σε αυτόν τον φάκελο υπάρχουν τα views και τα routes της εφαρμογής. Κάνουμε import
τις functions από τον φάκελο utiks για να φτιάξουμε τα endpoints. π.χ.

```python
from internal.lib.resize import resize

@app.route('/api/resize)
def resize_ep():
    ...
    ...
    return ...
```

Note: Τα endpoints πρέπει να είναι πάντα της μορφής '/api/functionallity'

### static
Στον φάκελο static υπάρχουν τα static αρχεία της εφαρμογής. Αυτά είναι js css και img.

```bash
├── css
│   └── main.css
├── img
│   ├── favicon
│   │   ├── android-chrome-192x192.png
│   │   ├── android-chrome-512x512.png
│   │   ├── apple-touch-icon.png
│   │   ├── favicon-16x16.png
│   │   ├── favicon-32x32.png
│   │   └── favicon.ico
│   └── qv1qx06t2
│       └── 2021-03-22_000.png
└── js
    ├── editor.js
    └── start.js
```

Υπάρχουν μόνο 2 αρχεία js: το `editor.js` και το `start.js`. Το `start.js` περιλαμβάνει κώδικα που αφορά το index/landing page από το οποίο ανεβάζουμε την φωτογραφία ενώ το `editor.js` αφορά κώδικα που έχει να κάνει με το editor page της εφαρμογής

### templates
Σε αυτόν τον φάκελο υπάρχει η HTML δομή της εφαρμογής

```bash
├── includes
│   └── head.html
├── base.html
├── editor.html
└── index.html
```

Όλα τα layouts κάνουν extend το `bash.html` από εκεί και πέρα υπάρχει το `index.html` (το οποίο περιέχει και το `start.js`) και το `editor.html` (το οποίο περιέχει το `editor.js`). Τέλος υπάρχουν και τα includes που χρησιμοποιούνται για κώδικα ο οποίος επαναλμβάνεται ή πρέπει να είναι σε μορφή components.

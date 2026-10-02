const datiOrazione = {
  // URL del Logo caricato su GitHub Pages per la Top Bar
  logoUrl: "https://21giaco76.github.io/app-preghiera/logo.png",

  links: {
    lodi: "https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia=20261001&ora=lodi-mattutine",
    vespri: "https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia=20261001&ora=vespri",
    compieta: "https://www.chiesacattolica.it/la-liturgia-delle-ore/?data-liturgia=20261001&ora=compieta",
    letture: "https://www.chiesacattolica.it/liturgia-del-giorno"
  },
  fotoSezioni: {
    lodi: "lodi.jpg",
    vespri: "vespri.jpg",
    compieta: "compieta.jpg",
    letture: "letture.jpg"
  },
 // Audio per le Letture della Messa (lascia vuoto "" se non c'è audio)
  audioLetture: "",

  // Sottocategorie: Misteri del Santo Rosario
  misteriRosario: [
    { 
      titolo: "Misteri Gaudiosi (Lunedì e Sabato)", 
      url: "https://archive.org/download/misteri-della-gioia-lunedi-e-sabato/misteri-della-gioia-lunedi-e-sabato.mp3" 
    },
    { 
      titolo: "Misteri Luminosi (Giovedì)", 
      url: "https://archive.org/download/misteri-luce-giovedi/misteri-luce-giovedi.mp3" 
    },
    { 
      titolo: "Misteri Dolorosi (Martedì e Venerdì)", 
      url: "https://archive.org/download/misteri-dolorosi-martedi-e-venerdi/misteri-dolorosi-martedi-e-venerdi.mp3" 
    },
    { 
      titolo: "Misteri Gloriosi (Mercoledì e Domenica)", 
      url: "https://archive.org/download/misteri-gloriosi-mercoledi-e-domenica/misteri-gloriosi-mercoledi-e-domenica.mp3" 
    }
  ],
  preghiereSettimanali: [
    {
      id: "lunedi",
      giorno: "Lunedì",
      titolo: "Preghiera del Lunedì della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "LUNEDI’ - Culto di amore",
      testoPreghiera2: "Signore nostro Gesù Cristo, insegnaci ad essere mansueti e umili di cuore per amare i nostri fratelli come Tu ci ami ed a trasformare tutta la nostra vita in una continua offerta agli altri. Ti chiediamo, oggi, di vivere intensamente questa consegna al servizio della nostra comunità. In unione con la Vergine nostra madre, Ti preghiamo in modo speciale per il Papa, i Vescovi, i Sacerdoti, i Diaconi, i Missionari, che hanno la vocazione di unire tutti gli uomini nell’amore. Cuore di Gesù, pieno di bontà e di amore, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si riceve,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "martedi",
      giorno: "Martedì",
      titolo: "Preghiera del Martedì della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "MARTEDÌ - Culto di riconoscenza",
      testoPreghiera2: "Signore nostro Gesù Cristo, uniti a Te vogliamo dar grazie al Padre per il dono della fede e per i tanti favori che a noi elargisci ogni giorno. Dà a noi la semplicità del bambino per riconoscere le meraviglie che Dio fece in noi e a vivere nella gioia dei salvati. Desideriamo, oggi, rinnovare la nostra fedeltà ai voti battesimali. Come la Vergine nel Suo Magnificat, e in unione ad Essa, desideriamo cantare la gloria di Dio per mezzo del nostro apostolato. Ti preghiamo per tutti quelli che lavorano al servizio della Chiesa, perché perseverino nella loro missione di inviati di Dio. Cuore di Gesù, dalla cui pienezza tutti abbiamo ricevuto, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo les grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si riceve,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "mercoledi",
      giorno: "Mercoledì",
      titolo: "Preghiera del Mercoledì della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "MERCOLEDÌ - Culto di speranza",
      testoPreghiera2: "Signore nostro Gesù Cristo, Tu sei la via, la verità, la vita. Insegnaci a portare a tutti gli uomini un messaggio di speranza, principalmente a coloro che cercano un segno, un significato nella loro vita e a quelli che soffrono in condizioni di vita inumana. Ti chiediamo, oggi, di accettare con pazienza le sofferenze morali e fisiche che si presentano per purificare la nostra anima e andare avanti nel cammino della santità. In unione alla Vergine dei dolori Ti chiediamo per i moribondi, i malati, e per gli oppressi, perché abbiano la forza nello spirito e sappiano trasformare i loro dolori in strumento di liberazione. Cuore di Gesù, salvezza di quelli che in Te sperano, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si receive,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "giovedi",
      giorno: "Giovedì",
      titolo: "Preghiera del Giovedì della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "GIOVEDÌ - Culto di Preghiera",
      testoPreghiera2: "Signore nostro Gesù Cristo, ricordando il Tuo invito a pregare senza interruzione, noi ci uniamo alla Tua  preghiera sacerdotale per offrirti questo giorno con le sue gioie e  con le sue pene  le fatiche e il riposo, trasformalo tutto in una continua preghiera al nostro Padre del cielo. Ti chiediamo, oggi, di fortificare la nostra fede per comunicarla a quelli che pongono la fiducia nella vanità del mondo disprezzando il valore della preghiera. Come la Vergine nel cenacolo, Ti esprimiamo la nostra confidenza, e in unione ad essa, Ti preghiamo per la grande famiglia cristiana, perché sappia apprezzare meglio il valore della preghiera. Cuore di Gesù, ricco di grazia per tutti quelli che Ti invocano, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si riceve,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "venerdi",
      giorno: "Venerdì",
      titolo: "Preghiera del Venerdì della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "VENERDÌ - Culto di giustizia",
      testoPreghiera2: "Signore nostro Gesù Cristo, contemplando il Tuo cuore aperto per il colpo di lancia, desideriamo completare nella nostra carne quello che manca alla Tua Passione. Dà a noi il coraggio di riparare alle nostre stesse ingiustizie ed a quelli dei nostri fratelli.Ti chiediamo, oggi, di riconoscere le ingiustizie che si commettono nella nostra comunità e intercedere per la liberazione di tutti i figli di Dio. In unione a nostra Signora del Sacro Cuore, Ti preghiamo per noi peccatori perché possiamo uscire dal nostro egoismo e cercare la felicità dei nostri fratelli. Cuore di Gesù, asilo di giustizia e di amore, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si receive,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassion.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "sabato",
      giorno: "Sabato",
      titolo: "Preghiera del Sabato della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "SABATO - Culto di unione",
      testoPreghiera2: "Signore nostro Gesù Cristo, facciamo nostra la  Tua preghiera al Padre perché siamo uno e perché il mondo riconosca che Dio stà in mezzo alla nostra comunità. Aiutaci a fortificare l'unione tra noi. Ti chiediamo, oggi, che cessino tutti i rancori e possiamo rinconciliarci con i nostri fratelli per mezzo di veritieri gesti di amicizia. In unione con la Vergine Madre, ti preghiamo per la comunità cristiana, perché si viva come fratelli in unione al Tuo Amore. Cuore di Gesù, pace e rinconciliazione nostra, abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si receive,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    },
    {
      id: "domenica",
      giorno: "Domenica",
      titolo: "Preghiera della Domenica della CSCV",

      titoloPreghiera1: "CONSACRAZIONE AL CUORE DI GESÙ",
      testoPreghiera1: "Ti salutiamo, Cuore ammirabile di Gesù. Ti lodiamo, Ti benediciamo, Ti glorifichiamo, Ti ringraziamo, Ti offriamo il nostro cuore, Te lo consegniamo e lo consacriamo a Te. Ricevilo e possiedilo intero; purificalo, illuminalo e santificalo, affinchè Tu viva e regni in esso perpetuamente.",
      foto1: "cascdg.jpg",

      titoloPreghiera2: "DOMENICA - Culto di adorazione",
      testoPreghiera2: "Signore nostro Gesù Cristo, in unione con Te, desideriamo adorare Dio, nostro Padre. In nome di tutta la creazione chiediamo, oggi, di manifestare pubblicamente la nostra adorazione filiale, specialmente durante l'assemblea della nostra comunità. In unione a Maria santissima, Ti preghiamo soprattutto per quelli che non conoscono Dio, nostro Padre, e per quelli che si sono dimenticati del Suo amore.  Cuore di Gesù, tempio santo di Dio abbi pietà di noi.",
      foto2: "madonnina.jpg",

      titoloPreghiera3: "preghiera A nostra Signora del Sacro Cuore",
      testoPreghiera3: "Ricordati Nostra Signora del Sacro Cuore delle meraviglie che Dio fece in Te. Te scelse come Madre del suo figlio. Te che lo seguisti fino alla croce. Te glorificò con lui ascoltando e accettando le tue preghiere per tutti gli uomini. Con grande confidenza nell'amore del Signore e nella Tua intercessione, veniamo con Te alla fonte del Suo cuore, da dove scaturiscono per la vita del mondo la speranza ed il perdono, la fedeltà e la salvezza. Nostra Signora del Sacro Cuore, tu conosci le nostre necessità, parla al Signore per noi e per tutti gli uomini. Aiutaci a vivere nel Suo amore, per esso riceviamo le grazie che chiediamo e quello che a noi è necessario. La Tua preghiera di madre è poderosa: che Dio risponda alla nostra speranza. Amen",

      titoloPreghiera4: "Preghiera Semplice",
      testoPreghiera4: "Oh Signore, fa di me un istrumento della tua pace:\nDove è odio, fa ch'io porti l'Amore.\nDove è offesa, ch'io porti il perdono.\nDove è discordia, ch'io porti l'Unione.\nDove è dubbio, ch'io porti la fede.\nDove è errore, ch'io porti la Verità.\nDove è disperazione, ch'io porti la Speranza.\nDove è tristezza, ch'io porti la Gioia.\nDove sono le tenebre, ch'io porti la Luce.\nOh! Maestro, fa ch'io non cerchi tanto,\nad essere consolato quanto a consolare,\nad essere compreso, quanto a comprendere,\nad essere amato, quanto ad amare.\nPoichè: E’ dando che si receive,\nperdonando che si è perdonati,\nmorendo, che si risuscita a vita eterna.",

      titoloPreghiera5: "Preghiera dell'ammalato",
      testoPreghiera5: "Signore Gesù, credo che sei vivo e risorto.\nTu sei la pienezza della vita,\nTu. Signore. sei la salute dei malati.\nOggi ti voglio presentare\ntutti i miei mali.\nAbbi compassione delle\nsofferenze del mio corpo,\ndel mio cuore e della mia anima.\nAbbi compassione di me, benedici mi\ne fa, Signore, che possa\nriacquistare la salute.\nChe cresca la mia fede e che\nmi apra alle meraviglie del tuo amore,\nperché sia anche testimone della tua potenza\ne della tua compassione.\nGuariscimi, Signore.\nGuariscimi nel corpo,\nguariscimi nel cuore,\nguariscimi nell'anima.\nDammi la vita. la vita in abbondanza.\nServo di Dio P. E. Tardif."
    }
  ]
};

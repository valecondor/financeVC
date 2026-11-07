# ETF Lab - versione HTML con aggiornamento automatico

## Pubblicazione (una volta sola)
1. Crea un repository **pubblico** su GitHub e carica tutti i file, inclusa la cartella `.github/workflows` (non solo `index.html`).
2. In **Settings > Pages**, seleziona **Deploy from a branch**, branch `main`, directory `/ (root)`.
3. In **Actions**, apri **Aggiorna quotazioni ETF** e scegli **Run workflow**. Attendi che finisca e controlla che `data/history.json` contenga prezzi. Se il workflow non riesce a scrivere, vai in **Settings > Actions > General > Workflow permissions** e seleziona **Read and write permissions**.
4. Apri `https://TUO-USERNAME.github.io/NOME-REPOSITORY/` dopo la pubblicazione.

L'aggiornamento è programmato dal lunedì al venerdì alle 07:30 UTC (GitHub può ritardarlo). Si può avviare manualmente in qualsiasi momento. La pagina non richiede Python sul tuo computer o iPhone.

## Uso locale
Il file `index.html` aperto con doppio clic può non riuscire a leggere `data/history.json` per restrizioni `file://`. Dopo aver installato le dipendenze ed eseguito `python update_data.py`, avvia nella cartella `python -m http.server 8000` e visita `http://localhost:8000`.

## Note sui dati
- Fonte: Yahoo Finance tramite libreria non ufficiale `yfinance`. Disponibilità non garantita; possibili limitazioni e problemi di licenza per la redistribuzione. Usare solo in conformità ai termini del fornitore.
- `auto_adjust=True`: prezzi rettificati per dividendi e split secondo Yahoo Finance, non equivalente a un backtest con costi e imposte reali.
- `EURUSD=X` è il numero di dollari per euro. I valori storici in EUR sono calcolati convertendo l'importo iniziale in USD alla data di acquisto e ogni valutazione successiva in EUR al cambio della data corrispondente.
- I simboli USA sono proxy e non necessariamente gli ETF UCITS acquistabili in Italia. Ogni ETF ha una propria data di inizio quotazioni.
- Se Yahoo fallisce per un simbolo, lo script conserva l'ultima serie già presente; l'aggiornamento può essere parziale. Controlla `errors` nel JSON.
- Le proiezioni future sono ipotetiche, non una previsione di mercato.

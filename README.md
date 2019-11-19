# parser
Analizador sintáctico implementado en python 2.7 con la libreria ply y PySide
El siguiente es un ejemplo de la sintaxis del lenguaje:



    INICIAR PROCESO(){
      IMPRIMIR("Hola"+" Mundo");

      VAR X <- 3, B <- A, C;

      C <- 11 - X / B * A;

      LEER(X);

      PARA(VAR i <- 0; i >= 100; i++){
        IMPRIMIR("Saludo");

        SI(A>B){
          IMPRIMIR(X+B+C); #concatenaciones
        }

        MIENTRAS(FIN < C ^^ X <> A // A < X){
          SI(x <> y){
            X <- 9 + A * B - D;
          }SINO_SI(x > 150 // x == 7){
            IMPRIMIR("Valores "+X);
          }SINO_SI(B >= C){
            IMPRIMIR("No hay Valores");
          }SINO{
            IMPRIMIR("FIN");
          }
          FIN <- FIN / 11;
          FIN--;
        }

      }
    }

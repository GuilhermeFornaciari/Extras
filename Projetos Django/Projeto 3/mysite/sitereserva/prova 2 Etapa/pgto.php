<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CSS</title>
<link href="css/styles.css" type="text/css" rel="stylesheet"> 
</head>
<body>
<div id="header">
    <p><img src="imagens/logo.png" class="tam_logo" alt="logo"/></p>
    <p class="slogan">Desperte seus sentidos na Pousada Sol e Mar: mergulhe na perfeição do sol, 
            sinta a brisa do mar, viva uma experiência única!</p>
    <div id="nav"> 
    <ul> 
        <li><a href="principal.php">Setor de Reservas</a></li>
        <li><a href="sobre.php">Sobre</a></li>
    </ul>
    </div>
</div>    

<?php
function busca_apto($codigo)
{
 $apto["1200-01"] ="Suíte com Banheira de Hidromassagem - 4 pessoas";
 $apto["1000-02"] ="Suíte com Banheira de Hidromassagem - 2 pessoas";
 $apto["850-03"] = "Quarto Duplo Deluxe - 1 Cama de casa extragrande - 2 pessoas";
 $apto["850-04"] = "Quarto Deluxe - 2 Camas de solteiro - 2 pessoas";
 $apto["720-05"] = "Quarto Superior com cama Queen-size - 2 pessoas";  
 return($apto[$codigo]);
}

// captura as informações enviadas pelo formulário

$acomodacao = $_POST['acomodacao'];
$dateE      = $_POST['dataE'];
$dateS      = $_POST['dataS'];
$nome       = $_POST['nome'];
$email      = $_POST['email'];
$telefone   = $_POST['telefone'];
//mostra as informações na tela
//echo busca_apto($acomodacao);
echo "<p class= 'pgto'>";
echo "Acomodoção: ".busca_apto($acomodacao) ."<br>";
$dataEntrada = date("d/m/y", strtotime($dateE));
echo "Data de Entrada: " .$dataEntrada ."<br>";
$dataSaida = date("d/m/y", strtotime($dateS));
echo "Data de Saída: " .$dataSaida ."<br>";
echo "Nome: " .$nome ."<br>";
echo "E-mail: " .$email ."<br>";
echo "Telefone: " .$telefone ."<br>";

$dtS = strtotime($dateS);
$dtE = strtotime($dateE);
$Segundos = $dtS - $dtE;
$dias = floor($Segundos / (60 * 60 * 24));

echo "Dias Reservados: " .$dias ."<br>";
$valor = substr($acomodacao, 0, strpos($acomodacao, "-"));

echo "Valor da Diária (R$): " .$valor ."<br>";
echo "<p class='valor'>" ."Valor da Reserva: " .$dias * $valor ."</p>";
echo "</p>";

?>

<div id="featured">     

    <div class="article2 column2">
        <table class="meio">
        <form action="fechamento.php" method="post"> 
        <fieldset class="cartao">
        <legend class="cartao">Pagamento</legend>
        <p>
        <div>
            <label for="cartao" class="title">Bandeira</label><br>
            <select class="cartao" name="cartao" id="cartao">
            <option value="mastercard">MasterCard</option>
            <option value="visa">Visa</option>
            </select>
        </div> 
        <div><br>
            <label class="title" for="numerocartao">Número do Cartão</label><br>
            <input type="text" id="numerocartao" name="numerocartao" maxlength="19" 
            pattern="\d{4}\.?\d{4}\.?\d{4}.?\d{4}" title="Digite o número no formato: xxxx.xxxx.xxxx.xxxx" required>
        </div>

        <div>
            <label class="title" for="codigocartao">Código do Cartão</label><br>
            <input type="text" id="codigocartao" name="codigocartao" maxlength="3" 
            pattern="\d{3}" title="Digite o número no formato: xxx" required>
        </div>
        <div>
            <label class="title" for="validade">Validade</label><br>
            <input type="text" id="validade" name="validade" maxlength="5" 
            pattern="\d{2}/?\d{2}" title="Digite o número no formato: xx/xx"required>
        </div>
        <div>
            <label class="title" for="nomecartao">Nome Impresso no Cartão</label><br>
            <input type="text" id="nomecartao" name="nomecartao" maxlength="30" 
            required>
        </div>
        </p>
        <div class="botoes">
            <input type="submit" value="Efetuar Pagamento" id="submit" />
            <input type="reset" value="Limpar Dados" id="reset" />
        </div>
        </fieldset>
        </form>
        </table>
    </div>  
</div>   
<div id="footer">
    <p>&copy; Copyright 2023 - Contato (e-mail): reservas@pousadasolmar.com.br</p>
</div>
<body></html>


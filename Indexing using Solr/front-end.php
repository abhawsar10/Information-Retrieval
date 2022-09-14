<?php

// make sure browsers see this page as utf-8 encoded HTML
header('Content-Type: text/html; charset=utf-8');
error_reporting(E_ERROR | E_WARNING | E_PARSE | E_NOTICE);

$limit = 10;
$query = isset($_REQUEST['q']) ? $_REQUEST['q'] : false;
$results = false;

if ($query)
{
  // The Apache Solr Client library should be on the include path
  // which is usually most easily accomplished by placing in the
  // same directory as this script ( . or current directory is a default
  // php include path entry in the php.ini)
  require_once('./Apache/Solr/Service.php');

  // create a new solr service instance - host, port, and webapp
  // path (all defaults in this example)
  $solr = new Apache_Solr_Service('localhost', 8983, '/solr/myexample/');

  // if magic quotes is enabled then stripslashes will be needed
  
  // in production code you'll always want to use a try /catch for any
  // possible exceptions emitted  by searching (i.e. connection
  // problems or a query parsing error)


  try
  {
	if ($_GET["algo_type"] == "PR") {
		$additionalParameters = array('sort' => 'pageRankFile desc');
		$results = $solr->search($query, 0, $limit, $additionalParameters);
	} else {
		$results = $solr->search($query, 0, $limit);
	}

  }
  catch (Exception $e)
  {
    // in production you'd probably log or email this error to an admin
    // and then show a special message to the user but for this example
    // we're going to show the full exception
    die("<html><head><title>SEARCH EXCEPTION</title><body><pre>{$e->__toString()}</pre></body></html>");
  }
}

?>
<html>
  <head>
    <title>PHP Solr Client Example</title>
  </head>
  <body>
    <form  accept-charset="utf-8" method="get">
      <label for="q">Search:</label>
      <input id="q" name="q" type="text" value="<?php echo htmlspecialchars($query, ENT_QUOTES, 'utf-8'); ?>"/>
	<br>
	Choose Algorithm:<br>
	<input type="radio" name="algo_type" value="L" > Lucene	<br>
	<input type="radio" name="algo_type" value="PR" > Page Rank <br>
      <input type="submit"/>
    </form>
<?php

// display results
if ($results)
{
  $total = (int) $results->response->numFound;
  $start = min(1, $total);
  $end = min($limit, $total);
?>
    <div>Results <?php echo $start; ?> - <?php echo $end;?> of <?php echo $total; ?>:</div>
    

<table style="text-align: left; width:100%; padding: 10px; cellpadding:10px">

<?php
  // iterate result documents
  
$i=0;
  foreach ($results->response->docs as $doc)
  {
	$i=$i+1;
	echo "<tr>";
	echo "<td>$i</td><td>";
	
	$id = $doc->id;
	$title = $doc->title;
	$url = $doc->og_url;
	$desc = $doc->og_description;	
	
	if ($desc == "" || $desc == null)
		$desc = "N/A";
	if ($title == "" || $title == null)
		$title = "N/A";


	if ($url == "" || $url == null) {

		$csv_file = array_map('str_getcsv', file('/home/anb/Downloads/FOXNEWS/URLtoHTML_fox_news.csv'));

		foreach ($csv_file as $data) {
			$full_loc = "/home/anb/Downloads/solr-7.7.3/foxnews/" . $data[0];
			if ($id == $full_loc) {
				$url = $data[1];
				break;
			}
		}
	}

?>
      
        <table style="border: 2px solid black; text-align: left; width:100%; padding: 10px; cellpadding:10px"> 
		
		<?php		

			echo "<tr style='border: 1px solid black;'>";
			echo "<th>Title</th>";
			echo "<td><a href = '$url' target='_blank'>$title</a></td>";
			echo "</tr>";

			echo "<tr>";
			echo "<th>URL</th>";
			echo "<td><a href = '$url' target='_blank'>$url</a></td>";
			echo "</tr>";

			echo "<tr>";
			echo "<th>ID</th>";
			echo "<td>$id</a></td>";
			echo "</tr>";

			echo "<tr>";
			echo "<th>DESC</th>";
			echo "<td>$desc</a></td>";
			echo "</tr>";

		?>


        </table> 
      
	</td>
	</tr>
<?php
  }
?>
</table>
<?php
}
?>
  </body>
</html>



#!/usr/bin/php -q
<?php

/********** CHANGE THESE ***************/
$_inputFile = $argv[1];
$_outputFile = $argv[2];
/**************************************/

// expects input file format to be: gram~year~title

if (($handle = fopen($_inputFile, "r")) !== FALSE) {
	
	// for each row
	while (($data = fgetcsv($handle, 1000, "~")) !== FALSE) {
		// add phrases to appropriate bin
	  $snippet = $data[0];
	  $terms[$data[1]][$data[2]][] = $data[0];
  }

  fclose($handle);
  ksort($terms);

	// open file for writing
  $fp = fopen($_outputFile, 'w+');
	
	// write new array to file
	fwrite($fp,  print_r($terms, true));
}
	fclose($fp);

?>

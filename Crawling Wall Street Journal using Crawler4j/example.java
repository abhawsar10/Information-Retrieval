package ab_crawler;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

import com.opencsv.CSVWriter;

public class example {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		String crawlStorageFolder = "fetch_wsj.csv"; 
		

	    File file = new File(crawlStorageFolder);
	    try {
	        // create FileWriter object with file as parameter
	    	
	        FileWriter outputfile = new FileWriter(file,true);
	        CSVWriter writer = new CSVWriter(outputfile);
	  
	        // adding header to csv
	        String[] header = { "URL", "HTTP Status Code" };
	        writer.writeNext(header);
	        
	        // add data to csv
//	        String[] data1 = { "Aman", "10", "620" };
//	        writer.writeNext(data1);
//	        String[] data2 = { "Suraj", "10", "630" };
//	        writer.writeNext(data2);
	  
	        // closing writer connection
	        writer.close();
	    }
	    catch (IOException e) {
	        // TODO Auto-generated catch block
	        e.printStackTrace();
	    }
		
		

	}

}
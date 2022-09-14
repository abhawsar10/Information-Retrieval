package ab_ass4;

import java.io.File;
import java.util.HashSet;
import java.util.Set;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

/**
 * Example program to list links from a URL.
 */
public class ExtractLinks {
	
    public static void main(String[] args) throws Exception {
    	
        File file = new File("Q:\\University of Southern California\\Classes\\CSCI 572 Information Retrieval\\HW4\\foxnews\\00beee34-8ac3-4261-bc0b-7ed7c7a6eb4d.html");
        Document doc = Jsoup.parse(file,"UTF-8","https://www.foxnews.com/");
        
        Elements links = doc.select("a[href]");
        

        print("\nLinks: (%d)", links.size());
        for (Element link : links) {
            print(" * a: <%s>  (%s)", link.attr("abs:href"), trim(link.text(), 35));
        }
        
        
    }
    
    private static void print(String msg, Object... args) {
        System.out.println(String.format(msg, args));
    }

    private static String trim(String s, int width) {
        if (s.length() > width)
            return s.substring(0, width-1) + ".";
        else
            return s;
    }
    
}
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

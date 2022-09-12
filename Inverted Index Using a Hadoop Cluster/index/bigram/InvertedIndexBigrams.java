import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

import java.io.IOException;
import java.util.HashMap;
import java.util.StringTokenizer;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;

public class bigrams_ab {
	
	public static class WordCountMapper extends Mapper<Object, Text, Text, Text>{

		private Text bigram = new Text();

		private Text doc_id = new Text();

		public void map(Object key, Text value, Context context) throws IOException, InterruptedException {
			
			String[] doc_full = value.toString().split("\t",2);

			doc_id.set(doc_full[0]);

			String doc_content = doc_full[1];

			doc_content = doc_content.toLowerCase();
			doc_content = doc_content.replaceAll("[^a-z\\s]", " ");
			doc_content = doc_content.replaceAll("\\s+", " ");


			StringTokenizer itr = new StringTokenizer(doc_content);
			String prev_word = itr.nextToken();

			while (itr.hasMoreTokens())
			{
				String curr_word = itr.nextToken();

				bigram.set(prev_word+" "+curr_word);
				context.write(bigram,doc_id);

				prev_word = curr_word;
			}
		}

	}
	
	public static class WordCountReducer extends Reducer<Text,Text,Text,Text> {
		
		private Text result = new Text();
		
		public void reduce(Text key, Iterable<Text> values, Context context) 
				throws IOException, InterruptedException {
			
			HashMap<String,Integer> word_count = new HashMap<>();

			for (Text val: values){

				String doc_id = val.toString();

				Integer prev_count = word_count.getOrDefault(doc_id, 0);
				word_count.put(doc_id, prev_count+ 1);
			}

			StringBuilder str = new StringBuilder();
			for (String ids : word_count.keySet())
				str.append(ids).append(":").append(word_count.get(ids)).append("\t");

			result.set(str.substring(0,str.length() - 1 ));
			context.write(key, result);
			
		}
	}
	

	public static void main(String[] args) throws IOException,ClassNotFoundException, InterruptedException {
	    
		if (args.length !=2){
			System.err.println("Usage: Word Count <input path> <output path>");
			System.exit(-1);
		}
		

	    Configuration conf = new Configuration();

		Job job = Job.getInstance(conf,"Inverted Index Bigrams");
	    
    	job.setJarByClass(bigrams_ab.class);

    	job.setMapperClass(WordCountMapper.class);
    	job.setReducerClass(WordCountReducer.class);
	
    	job.setOutputKeyClass(Text.class);
    	job.setOutputValueClass(Text.class);

    	FileInputFormat.addInputPath(job, new Path(args[0]));
    	FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);


	}
	
	
}

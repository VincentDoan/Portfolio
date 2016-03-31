using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    /// <summary>
    /// The TestData class will take in objects of DataAcquistion, UUTInformation, ChannelData, and the number of channels.
    /// The class will take into account number of channels and finally Serialize all the data into CSV format.
    /// </summary>
    /*public static class Global
    {
        public static int size;
    }*/

    public class TestData
    {
        TestConfig config;

        public TestConfig Config
        {
            get { return config; }
            set { config = value; }
        }
        
        UUTInformation uut;

        public UUTInformation Uut
        {
            get { return uut; }
            set { uut = value; }
        }
       
        ChannelDataList channels;

        public ChannelDataList Channels
        {
            get { return channels; }
            set { channels = value; }
        }

        TransducerTestSetting transducer;

        internal TransducerTestSetting Transducer
        {
            get { return transducer; }
            set { transducer = value; }
        }

        List<TransducerTestSetting> transducerList = new List<TransducerTestSetting>();


        public TestData()
        {

        }

        public TestData(TestConfig config, UUTInformation uut, ChannelDataList channels, int newSize)
        {
            this.config = config;
            this.uut = uut;
            this.channels = channels;
            TestConfig.ChannelCount = newSize;

            for (int i = 0; i < TestConfig.ChannelCount; ++i)
            {
                if (config.TransSettings[i].Enabled == false)
                {
                    for (int j = 0; j < newSize; ++j)
                    {
                        channels.Channels[i] = null;
                    }
                    //Console.WriteLine("///////ENABLED\\\\\\\\\\: " + i + " " + dac.Enabled[i]);
                    //Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
                }
              //  Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
            }
                
        }

        public TestData(TestConfig config, UUTInformation uut, ChannelDataList channels, TransducerTestSetting transducer, int newSize)
        {
            this.config = config;
            this.uut = uut;
            this.channels = channels;
            this.transducer = transducer;
            TestConfig.ChannelCount = newSize;

            for (int i = 0; i < TestConfig.ChannelCount; ++i)
            {
                if (config.TransSettings[i].Enabled == false)
                {
                    for (int j = 0; j < newSize; ++j)
                    {
                        channels.Channels[i] = null;
                    }
                    //Console.WriteLine("///////ENABLED\\\\\\\\\\: " + i + " " + dac.Enabled[i]);
                    //Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
                }
                //  Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
            }

        }

        /// <summary>
        /// function that serializes a the test using all objects to CSV file format to directory of file name.
        /// </summary>
        /// <param name="fileName"></param>

        public void SerializeToCSV(string fileName)
        {
            //fileName = "C:\\Users\\Vincent\\Desktop\\stuff\\test.csv";
            using (System.IO.StreamWriter file = new System.IO.StreamWriter(@fileName))
            {
                file.WriteLine(uut.TestTime);
                file.WriteLine("Motor: " + uut.MotorName);
                file.WriteLine("Serial Number: " + uut.SerialNo);
                file.WriteLine();
                file.WriteLine("Sample Rate: " + config.SampleRate);
                file.WriteLine("Duration: " + config.Duration);
                file.WriteLine("Total Samples Per Channel: " + config.TotalSamples);
                file.Write("Calibrations: ");
                for (int i = 0; i < config.Calibrations.Count; ++i)
                {
                    file.Write(config.Calibrations[i] + "    ");
                }
                file.WriteLine();
                /*file.Write("Coefficients: ");
                for (int i = 0; i < dac.Coefficients.Count; ++i)
                {
                    file.Write(dac.Coefficients[i] + "    ");
                }*/
                file.WriteLine();
                file.WriteLine();
                file.Write("Enabled Channels:  ");
                for (int i = 0; i < TestConfig.ChannelCount - 1; ++i)
                {
                    file.Write("<[Channel " + (i + 1) + "]:  ");
                    file.Write(config.TransSettings[i].Enabled + ">    ");
                }
                file.WriteLine();
                file.WriteLine();

               // file.WriteLine("Time       Current       Channel 1       Channel 2       Channel 3       Channel 4       Channel 5       Channel 6       Channel 7       Channel 8       Channel 9");
                file.Write("Time,Current,");
                for (int j = 0; j < 9; ++j)
                {
                    if (config.TransSettings[j].Enabled == false)
                        file.Write("Channel" + (j + 1) + ",");
                }

                double time = 0.0;

                file.WriteLine();
                //Initialize the CSV files to 0's
                file.Write(String.Format("{0:F3},", time));
                file.Write(String.Format("{0:F3},", 0));

                for (int j = 0; j < 9; ++j)
                {
                    if (config.TransSettings[j].Enabled)
                    {
                        file.Write(String.Format("{0:F3},", 0));
                    }
                }
                time += config.Duration / config.TotalSamples;
                file.WriteLine();


                for (int i = 0; i < config.TotalSamples; ++i)
                {
                    file.Write(String.Format("{0:F3},", time));
                    file.Write(String.Format("{0:F3},", i));
                    time += config.Duration / config.TotalSamples;

                    for (int j = 0; j < 9; ++j)
                    {
                        if (config.TransSettings[j].Enabled)
                            {
                                file.Write(String.Format("{0:F3},", channels.Channels[j].Samples[i]));
                            }
                        /*else
                            {
                                file.Write("                ");
                            }*/
                    }
                    
                    /*for (int j = 0; j < 9; ++j)
                    {
                        if (dac.Enabled[i])
                        {
                            file.Write(channels.Channels[i].Samples[j]);
                        }
                        else
                        {
                            file.Write("                ");
                        }
                    }*/
                    file.WriteLine();

                   // file.WriteLine();
                    //time += dac.Duration / dac.TotalSamples;
                
               
                    //May need to look into spaces at end
                    /*if (dac.Enabled[i])
                        for (int j = 0; j < channels.Channels[i].Samples.Count; ++j)
                        {
                              file.WriteLine(String.Format("{0:F3}       ", channels.Channels[i].Samples[j]));
                        }  */
                }

                //for (int i = 0; i < channels.Channels.Count; ++i)
                //{
                //    if (dac.Enabled[i])
                 //       for (int j = 0; j < channels.Channels[i].Samples.Count; ++j)
                 //       {
                 //           file.WriteLine("<[Channel " + i + "| Data " + j + "]: " + channels.Channels[i].Samples[j].ToString() + ">");
                 //       }
                   /* else
                        for (int j = 0; j < dac.TotalSamples; ++j)
                        {
                            file.WriteLine("<[Channel " + i + "| Data " + j + "]: " + "0>");
                        }*/
               // }
               // file.WriteLine("");
            }
        }
        
    }
}

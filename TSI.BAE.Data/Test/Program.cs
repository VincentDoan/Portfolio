using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TSI.BAE.Data;

namespace Test
{
    /// <summary>
    /// A Console Test program for the classes
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            int ChannelCount=10;
            string[] UUTTypes = { "MK90 Thrust Only", "MK90", "HPC Bomb" };
            string[] ChannelNames = { "Current",
                                    "Load channel 1 (Load cell 1)",
                                    "Load channel 2 (Load cell 2)",
                                    "Load channel 3 (Pressure transducer 1)",
                                    "Load channel 4 (Pressure transducer 2)",
                                    "Load channel 5 (spare)",
                                    "Load channel 6 (spare)",
                                    "Load channel 7 (spare)",
                                    "Load channel 8 (spare)",
                                    "Load channel 9 (HPC Bomb analog input)"
                                    };

            int sampleRate = 5000;
            double duration = 1.2;
            List<double> calibrations = new List<double>();
            calibrations.Add(1.1);
            calibrations.Add(1.2);
            calibrations.Add(1.3);
            
            List<TransducerSettings> transducerSettings = new List<TransducerSettings>();

            for (int i = 0; i < ChannelCount; i++)
            {
                transducerSettings.Add(new TransducerSettings(ChannelNames[i], i, "None"));
            }



            /* 
            List<TransducerTestSetting> testSetting = new List<TransducerTestSetting>();
            double offset = 0.0;
            int trackingId = 1000;
            for (int i = 0; i < 10; ++i)
            {
                List<double> gf = new List<double>();
                for (int j = 0; j < 9; ++j)
                {
                    gf.Add(j);
                }

                List<double> averages = new List<double>();
                for (int j = 10; j < 20; ++j)
                {
                    averages.Add(j);
                }
            }
            
            TransducerTestSetting transducer = new TransducerTestSetting(gf, averages, offset, trackingId);
            tranducerTestSetting.Add(transducer);*/


            /*List<double> coefficients = new List<double>();
            coefficients.Add(2.2);
            coefficients.Add(2.3);
            coefficients.Add(2.4);*/
            /*List<bool> enabled = new List<bool>();
            enabled.Add(true);
            enabled.Add(true);
            enabled.Add(false);
            enabled.Add(true);
            enabled.Add(true);
            enabled.Add(false);
            enabled.Add(true);
            enabled.Add(true);
            enabled.Add(false);
            enabled.Add(true);*/
            //List<bool> enabled2 = new List<bool>();

            //TestConfig config = new TestConfig(sampleRate, duration, calibrations, enabled, 10);
            UUTInformation uut = new UUTInformation();
           // TestConfig config = new TestConfig("ConfigurationA", 6.0, 500, 80, 100, sampleRate, duration, "MK90 Thrust Only", calibrations, TestConfig.ChannelCount, transducerSettings);
  
            TestConfig.Serialize("C:\\Users\\Vincent\\Desktop\\stuff\\test3.xml", uut);

            //TestConfig config1 = new TestConfig();
            //config1 = TestConfig.Deserialize("C:\\Users\\Vincent\\Desktop\\stuff\\test.xml");

           /* Console.WriteLine();
            Console.WriteLine("Data Acquisition Configuration:");
            Console.WriteLine(config1.SampleRate.ToString());
            Console.WriteLine(config1.Calibrations[0].ToString());
            Console.WriteLine(config1.Calibrations[1].ToString());
            Console.WriteLine(config1.Calibrations[2].ToString());

            Console.WriteLine(config1.Enabled[0].ToString());
            Console.WriteLine(config1.Enabled[1].ToString());
            Console.WriteLine(dac1.Enabled[2].ToString());
            Console.WriteLine();*/

            //UUT
            //DateTime testTime = new DateTime(2015, 09, 13);
            /*string motorName = "motor";
            string serialNo = "000001";
            UUTInformation uut = new UUTInformation(motorName, serialNo);

            Console.WriteLine("UUT Information:");
            Console.WriteLine("Test Time: " + uut.TestTime.ToString());
            Console.WriteLine("Motor: " + uut.MotorName.ToString());
            Console.WriteLine("Serial Number: " + uut.SerialNo.ToString());
            Console.WriteLine();

            //CHANNELS
            ChannelData data0 = new ChannelData();
            data0.Samples.Add(1.1);
            data0.Samples.Add(2.2);
            data0.Samples.Add(3.3);

            ChannelData data1 = new ChannelData();
            data1.Samples.Add(4.4);
            data1.Samples.Add(5.5);
            data1.Samples.Add(6.6);

            ChannelData data2 = new ChannelData();
            data2.Samples.Add(7.7);
            data2.Samples.Add(8.8);
            data2.Samples.Add(9.9);

            ChannelData data3 = new ChannelData();
            data3.Samples.Add(10.10);
            data3.Samples.Add(11.11);
            data3.Samples.Add(12.12);

            ChannelData data4 = new ChannelData();
            data4.Samples.Add(13.13);
            data4.Samples.Add(14.14);
            data4.Samples.Add(15.15);

            ChannelData data5 = new ChannelData();
            data5.Samples.Add(16.16);
            data5.Samples.Add(17.17);
            data5.Samples.Add(18.18);

            ChannelData data6 = new ChannelData();
            data6.Samples.Add(19.19);
            data6.Samples.Add(20.20);
            data6.Samples.Add(21.21);

            ChannelData data7 = new ChannelData();
            data7.Samples.Add(22.22);
            data7.Samples.Add(23.23);
            data7.Samples.Add(24.24);

            ChannelData data8 = new ChannelData();
            data8.Samples.Add(25.25);
            data8.Samples.Add(26.26);
            data8.Samples.Add(27.27);

            ChannelData data9 = new ChannelData();
            data9.Samples.Add(28.28);
            data9.Samples.Add(29.29);
            data9.Samples.Add(30.30);


            ChannelDataList channels = new ChannelDataList();
            channels.Channels.Add(data0);
            channels.Channels.Add(data1);
            channels.Channels.Add(data2);
            channels.Channels.Add(data3);
            channels.Channels.Add(data4);
            channels.Channels.Add(data5);
            channels.Channels.Add(data6);
            channels.Channels.Add(data7);
            channels.Channels.Add(data8);
            channels.Channels.Add(data9);

            Console.WriteLine(channels.Channels[0].Samples[0].ToString());
            Console.WriteLine(channels.Channels[1].Samples[0].ToString());
            Console.WriteLine(channels.Channels[2].Samples[0].ToString());
            Console.WriteLine(channels.Channels[3].Samples[0].ToString());
            Console.WriteLine(channels.Channels[4].Samples[0].ToString());
            Console.WriteLine(channels.Channels[5].Samples[0].ToString());
            Console.WriteLine(channels.Channels[6].Samples[0].ToString());
            Console.WriteLine(channels.Channels[7].Samples[0].ToString());
            Console.WriteLine(channels.Channels[8].Samples[0].ToString());
            Console.WriteLine(channels.Channels[9].Samples[0].ToString());


            //TEST DATA
            //TestData test = new TestData(config, uut, channels, 10);

            ChannelData sample10 = new ChannelData();*/
          
           /* Console.WriteLine("UUT Test Time: " + test.Uut.TestTime.ToString());
            Console.WriteLine("UUT Motor Name: " + test.Uut.MotorName.ToString());
            Console.WriteLine("UUT Serial Number: " + test.Uut.SerialNo.ToString());
            Console.WriteLine();

            Console.WriteLine("Sample Rate: " + test.Dac.SampleRate.ToString());
            Console.WriteLine("Calibrations: " + test.Dac.Calibrations[0].ToString());
            Console.WriteLine("Coefficients: " + test.Dac.Coefficients[0].ToString());
            Console.WriteLine();*/

            /*for (int i = 0; i < test.Dac.Enabled.Count; ++i)
            {
                Console.WriteLine("Channels: " + test.Dac.Enabled[i].ToString());
            }
            Console.WriteLine();

            
            for (int i = 0; i < test.Channels.Channels.Count; ++i)
            {
               if (test.Dac.Enabled[i])
                    /*for (int j = 0; j < 3; ++j)
                    {
                        Console.WriteLine("<[Channel " + i + "| Data " + j + "]: " + test.Channels.Channels[i].Samples[j].ToString() + ">");
                    }*/
                   /* for (int j = 0; j < test.Channels.Channels[i].Samples.Count; ++j)
                    {
                        Console.WriteLine("<[Channel " + i + "| Data " + j + "]: " + test.Channels.Channels[i].Samples[j].ToString() + ">");
                    }
            }*/








           /* Console.WriteLine(Global.size);
            for (int i = 0; i < Global.size; ++i)
            {
                Console.WriteLine(test.Dac.Enabled[i].ToString());
                /*if (test.Dac.Enabled[i] == true)
                {
                    Console.WriteLine("///////ENABLED\\\\\\\\\\: " + i + " " + dac.Enabled[i]);
                   
                    //Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
                }
                //  Console.WriteLine("Channel " + i + ": " + this.channels.Channels[i]);
            }
            Console.WriteLine("YO BRO");*/
            
            //Console.WriteLine("Channels: " + test.Channels.Channels[0].Samples[0].ToString());
           // Console.WriteLine("Channels: " + test.Channels.Channels[0].Samples[1].ToString());
           // Console.WriteLine("Channels: " + test.Channels.Channels[0].Samples[2].ToString());
           // Console.WriteLine("Channels WRONG: " + test.Channels.Channels[8].Samples[0].ToString());
            //Console.WriteLine("Channels: " + test.Channels.Channels[9].Samples[1].ToString());
            //Console.WriteLine("Channels: " + test.Channels.Channels[9].Samples[2].ToString());
            //Console.WriteLine("Channels: " + test.Channels.Channels[6].Samples[1].ToString());
           // Console.WriteLine("Channels: " + test.Channels.Channels[2].Samples[0].ToString());
           
            //test.SerializeToCSV("yo bro");
        }
    }
}
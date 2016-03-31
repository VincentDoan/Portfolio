using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    /// <summary>
    /// Class containing a List of samples (double).
    /// </summary>
   
   public class ChannelData
    {

       List<double> samples = new List<double>();

        public List<double> Samples
        {
            get { return samples; }
            set { samples = value; }
        }

       public ChannelData()
       {

       }

       public ChannelData(int sampleSize)
       {
           samples.Capacity = sampleSize;
       }
    }
}

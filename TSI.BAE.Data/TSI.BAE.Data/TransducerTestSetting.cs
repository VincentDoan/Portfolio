using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TSI.BAE.Data
{
    public class TransducerTestSetting : TransducerSettings
    {
        List<double> gf = new List<double>();

        public List<double> Gf
        {
            get { return gf; }
            set { gf = value; }
        }
        
        List<double> averages = new List<double>();

        public List<double> Averages
        {
            get { return averages; }
            set { averages = value; }
        }

        double offset;

        public double Offset
        {
            get { return offset; }
            set { offset = value; }
        }

        int trackingId;

        public int TrackingId
        {
            get { return trackingId; }
            set { trackingId = value; }
        }

        public TransducerTestSetting(string name, int chan, string type, List<double> gf, List<double> averages, double offset, int trackingId)
        {
            Type = type;
            ChannelID = chan;
            Name = name;
            this.gf = gf;
            this.averages = averages;
            this.offset = offset;
            this.trackingId = trackingId;
        }

        public TransducerTestSetting(List<double> gf, List<double> averages, double offset, int trackingId)
        {
            this.gf = gf;
            this.averages = averages;
            this.offset = offset;
            this.trackingId = trackingId;
        }
        // Needs GF array 
        // Needs Averages array
        // Need Offset
        // Tracking ID


    }
}

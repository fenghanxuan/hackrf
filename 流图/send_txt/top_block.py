#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jan 24 13:11:41 2018
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import sip
import sys
import time


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 25000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_0_0 = filter.rational_resampler_ccc(
                interpolation=8,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.qtgui_time_sink_x_3_0 = qtgui.time_sink_f(
        	500, #size
        	samp_rate, #samp_rate
        	"after_interpolator", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_3_0.set_update_time(0.10)
        self.qtgui_time_sink_x_3_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_3_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_3_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_3_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_3_0.enable_autoscale(False)
        self.qtgui_time_sink_x_3_0.enable_grid(False)
        self.qtgui_time_sink_x_3_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_3_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_3_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_3_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_3_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_3_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_3_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_3_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_3_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_3_0_win = sip.wrapinstance(self.qtgui_time_sink_x_3_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_3_0_win)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_c(
        	500, #size
        	samp_rate, #samp_rate
        	"after_FM", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        self.qtgui_time_sink_x_0_0.enable_control_panel(False)
        
        if not True:
          self.qtgui_time_sink_x_0_0.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(2*1):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + "" )
        self.osmosdr_sink_0.set_sample_rate(1e6)
        self.osmosdr_sink_0.set_center_freq(1000e6, 0)
        self.osmosdr_sink_0.set_freq_corr(6, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(40, 0)
        self.osmosdr_sink_0.set_bb_gain(30, 0)
        self.osmosdr_sink_0.set_antenna("", 0)
        self.osmosdr_sink_0.set_bandwidth(250e3, 0)
          
        self.fractional_interpolator_xx_0 = filter.fractional_interpolator_ff(1, 0.875)
        self.file_input = qtgui.time_sink_f(
        	500, #size
        	samp_rate, #samp_rate
        	"file_input", #name
        	1 #number of inputs
        )
        self.file_input.set_update_time(0.10)
        self.file_input.set_y_axis(-1, 1)
        
        self.file_input.set_y_label("Amplitude", "")
        
        self.file_input.enable_tags(-1, True)
        self.file_input.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.file_input.enable_autoscale(False)
        self.file_input.enable_grid(False)
        self.file_input.enable_control_panel(False)
        
        if not True:
          self.file_input.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.file_input.set_line_label(i, "Data {0}".format(i))
            else:
                self.file_input.set_line_label(i, labels[i])
            self.file_input.set_line_width(i, widths[i])
            self.file_input.set_line_color(i, colors[i])
            self.file_input.set_line_style(i, styles[i])
            self.file_input.set_line_marker(i, markers[i])
            self.file_input.set_line_alpha(i, alphas[i])
        
        self._file_input_win = sip.wrapinstance(self.file_input.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._file_input_win)
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0, 0, 0), True, 1, [])
        self.blocks_stream_mux_0 = blocks.stream_mux(gr.sizeof_float*1, (1, 1))
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, 10)
        self.blocks_multiply_xx_0_0 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, "/home/andy/code.txt", True)
        self.blocks_char_to_float_0 = blocks.char_to_float(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((-0.5, ))
        self.bipolar_wave = qtgui.time_sink_f(
        	500, #size
        	samp_rate, #samp_rate
        	"bipolar_wave", #name
        	1 #number of inputs
        )
        self.bipolar_wave.set_update_time(0.10)
        self.bipolar_wave.set_y_axis(-1, 1)
        
        self.bipolar_wave.set_y_label("Amplitude", "")
        
        self.bipolar_wave.enable_tags(-1, True)
        self.bipolar_wave.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.bipolar_wave.enable_autoscale(False)
        self.bipolar_wave.enable_grid(False)
        self.bipolar_wave.enable_control_panel(False)
        
        if not True:
          self.bipolar_wave.disable_legend()
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.bipolar_wave.set_line_label(i, "Data {0}".format(i))
            else:
                self.bipolar_wave.set_line_label(i, labels[i])
            self.bipolar_wave.set_line_width(i, widths[i])
            self.bipolar_wave.set_line_color(i, colors[i])
            self.bipolar_wave.set_line_style(i, styles[i])
            self.bipolar_wave.set_line_marker(i, markers[i])
            self.bipolar_wave.set_line_alpha(i, alphas[i])
        
        self._bipolar_wave_win = sip.wrapinstance(self.bipolar_wave.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._bipolar_wave_win)
        self.analog_wfm_tx_0 = analog.wfm_tx(
        	audio_rate=int(25e3),
        	quad_rate=int(500e3),
        	tau=3e-6,
        	max_dev=50e3,
        )
        self.analog_sig_source_x_0_0 = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 1000, 1, 0)
        self.analog_sig_source_x_0 = analog.sig_source_f(samp_rate, analog.GR_CONST_WAVE, 1000, 1, 0)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_multiply_xx_0_0, 1))    
        self.connect((self.analog_wfm_tx_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.analog_wfm_tx_0, 0), (self.rational_resampler_xxx_0_0, 0))    
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_char_to_float_0, 0), (self.file_input, 0))    
        self.connect((self.blocks_file_source_0, 0), (self.blocks_char_to_float_0, 0))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_stream_mux_0, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.bipolar_wave, 0))    
        self.connect((self.blocks_multiply_xx_0_0, 0), (self.fractional_interpolator_xx_0, 0))    
        self.connect((self.blocks_repeat_0, 0), (self.blocks_multiply_xx_0_0, 0))    
        self.connect((self.blocks_stream_mux_0, 0), (self.blocks_repeat_0, 0))    
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_stream_mux_0, 1))    
        self.connect((self.fractional_interpolator_xx_0, 0), (self.analog_wfm_tx_0, 0))    
        self.connect((self.fractional_interpolator_xx_0, 0), (self.qtgui_time_sink_x_3_0, 0))    
        self.connect((self.rational_resampler_xxx_0_0, 0), (self.osmosdr_sink_0, 0))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()


    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
        self.file_input.set_samp_rate(self.samp_rate)
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.qtgui_time_sink_x_3_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.bipolar_wave.set_samp_rate(self.samp_rate)


def main(top_block_cls=top_block, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()

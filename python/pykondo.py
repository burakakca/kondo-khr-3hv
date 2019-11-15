# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pykondo', [dirname(__file__)])
        except ImportError:
            import _pykondo
            return _pykondo
        if fp is not None:
            try:
                _mod = imp.load_module('_pykondo', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pykondo = swig_import_helper()
    del swig_import_helper
else:
    import _pykondo
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


RCB4_SECOND = _pykondo.RCB4_SECOND
RCB4_15MS = _pykondo.RCB4_15MS
RCB4_50MS = _pykondo.RCB4_50MS
RCB4_USB_VID = _pykondo.RCB4_USB_VID
RCB4_USB_PID = _pykondo.RCB4_USB_PID
RCB4_BAUD = _pykondo.RCB4_BAUD
RCB4_SWAP_SIZE = _pykondo.RCB4_SWAP_SIZE
RCB4_RX_TIMEOUT = _pykondo.RCB4_RX_TIMEOUT
RCB4_ACK_BYTE = _pykondo.RCB4_ACK_BYTE
RCB4_NCK_BYTE = _pykondo.RCB4_NCK_BYTE
RCB4_CMD_ACK = _pykondo.RCB4_CMD_ACK
RCB4_CMD_MOV = _pykondo.RCB4_CMD_MOV
RCB4_CMD_CALL = _pykondo.RCB4_CMD_CALL
RCB4_CMD_VERS = _pykondo.RCB4_CMD_VERS
RCB4_CMD_ICS = _pykondo.RCB4_CMD_ICS
RCB4_DEV_RAM = _pykondo.RCB4_DEV_RAM
RCB4_DEV_DEV = _pykondo.RCB4_DEV_DEV
RCB4_DEV_COM = _pykondo.RCB4_DEV_COM
RCB4_DEV_ROM = _pykondo.RCB4_DEV_ROM
RCB4_RAM_TO_COM = _pykondo.RCB4_RAM_TO_COM
RCB4_COM_TO_RAM = _pykondo.RCB4_COM_TO_RAM
RCB4_OPT_BYTES = _pykondo.RCB4_OPT_BYTES
RCB4_OPT_SIO = _pykondo.RCB4_OPT_SIO
RCB4_OPT_EEPROM = _pykondo.RCB4_OPT_EEPROM
RCB4_OPT_RESP = _pykondo.RCB4_OPT_RESP
RCB4_OPT_VEC = _pykondo.RCB4_OPT_VEC
RCB4_OPT_FRAME_10MS = _pykondo.RCB4_OPT_FRAME_10MS
RCB4_OPT_FRAME_20MS = _pykondo.RCB4_OPT_FRAME_20MS
RCB4_OPT_FRAME_15MS = _pykondo.RCB4_OPT_FRAME_15MS
RCB4_OPT_FRAME_25MS = _pykondo.RCB4_OPT_FRAME_25MS
RCB4_OPT_COM_BAUD_125200 = _pykondo.RCB4_OPT_COM_BAUD_125200
RCB4_OPT_COM_BAUD_625000 = _pykondo.RCB4_OPT_COM_BAUD_625000
RCB4_OPT_COM_BAUD_1250000 = _pykondo.RCB4_OPT_COM_BAUD_1250000
RCB4_OPT_ZERO = _pykondo.RCB4_OPT_ZERO
RCB4_OPT_CARRY = _pykondo.RCB4_OPT_CARRY
RCB4_OPT_ERROR = _pykondo.RCB4_OPT_ERROR
RCB4_OPT_ICS_BAUD_125200 = _pykondo.RCB4_OPT_ICS_BAUD_125200
RCB4_OPT_ICS_BAUD_625000 = _pykondo.RCB4_OPT_ICS_BAUD_625000
RCB4_OPT_ICS_BAUD_1250000 = _pykondo.RCB4_OPT_ICS_BAUD_1250000
RCB4_OPT_GREEN_LED = _pykondo.RCB4_OPT_GREEN_LED
RCB4_OPT_LOW = _pykondo.RCB4_OPT_LOW
RCB4_OPT_HIGH = _pykondo.RCB4_OPT_HIGH
RCB4_ADDR_OPT = _pykondo.RCB4_ADDR_OPT
RCB4_ADDR_PGC = _pykondo.RCB4_ADDR_PGC
RCB4_ADDR_EEPROM_FLAG = _pykondo.RCB4_ADDR_EEPROM_FLAG
RCB4_ADDR_AD_REF_BASE = _pykondo.RCB4_ADDR_AD_REF_BASE
RCB4_ADDR_AD_READ_BASE = _pykondo.RCB4_ADDR_AD_READ_BASE
RCB4_NUM_ANALOGS = _pykondo.RCB4_NUM_ANALOGS
RCB4_ADDR_PIO_SET = _pykondo.RCB4_ADDR_PIO_SET
RCB4_ADDR_PIO_OUTPUT = _pykondo.RCB4_ADDR_PIO_OUTPUT
RCB4_ADDR_TIMER_0 = _pykondo.RCB4_ADDR_TIMER_0
RCB4_ADDR_TIMER_1 = _pykondo.RCB4_ADDR_TIMER_1
RCB4_ADDR_TIMER_2 = _pykondo.RCB4_ADDR_TIMER_2
RCB4_ADDR_TIMER_3 = _pykondo.RCB4_ADDR_TIMER_3
RCB4_ADDR_ICS_BASE = _pykondo.RCB4_ADDR_ICS_BASE
RCB4_NUM_ICS = _pykondo.RCB4_NUM_ICS
RCB4_ADDR_MAIN = _pykondo.RCB4_ADDR_MAIN
RCB4_ADDR_SERVO = _pykondo.RCB4_ADDR_SERVO
RCB4_SERVO_DATA_SIZE = _pykondo.RCB4_SERVO_DATA_SIZE
RCB4_NUM_SERVOS = _pykondo.RCB4_NUM_SERVOS
RCB4_ADDR_KRI = _pykondo.RCB4_ADDR_KRI
RCB4_ADDR_BTN_L = _pykondo.RCB4_ADDR_BTN_L
RCB4_ADDR_BTN_M = _pykondo.RCB4_ADDR_BTN_M
RCB4_ADDR_BTN_H = _pykondo.RCB4_ADDR_BTN_H
RCB4_ADDR_MOT_BASE = _pykondo.RCB4_ADDR_MOT_BASE
RCB4_MOT_SIZE = _pykondo.RCB4_MOT_SIZE
RCB4_MOT_MAX = _pykondo.RCB4_MOT_MAX
RCB4_SERVO_ID_OFFSET = _pykondo.RCB4_SERVO_ID_OFFSET
RCB4_SERVO_SETPOS_OFFSET = _pykondo.RCB4_SERVO_SETPOS_OFFSET
RCB4_SERVO_POS_OFFSET = _pykondo.RCB4_SERVO_POS_OFFSET
RCB4_SERVO_TRIM_OFFSET = _pykondo.RCB4_SERVO_TRIM_OFFSET
RCB4_ADDR_COUNTER_BASE = _pykondo.RCB4_ADDR_COUNTER_BASE
RCB4_NUM_COUNTERS = _pykondo.RCB4_NUM_COUNTERS
RCB4_BTN_NP = _pykondo.RCB4_BTN_NP
RCB4_BTN_LU = _pykondo.RCB4_BTN_LU
RCB4_BTN_LD = _pykondo.RCB4_BTN_LD
RCB4_BTN_LR = _pykondo.RCB4_BTN_LR
RCB4_BTN_LL = _pykondo.RCB4_BTN_LL
RCB4_BTN_RU = _pykondo.RCB4_BTN_RU
RCB4_BTN_RD = _pykondo.RCB4_BTN_RD
RCB4_BTN_RR = _pykondo.RCB4_BTN_RR
RCB4_BTN_RL = _pykondo.RCB4_BTN_RL
RCB4_BTN_S1 = _pykondo.RCB4_BTN_S1
RCB4_BTN_S2 = _pykondo.RCB4_BTN_S2
RCB4_BTN_S3 = _pykondo.RCB4_BTN_S3
RCB4_BTN_S4 = _pykondo.RCB4_BTN_S4
class KondoInstance(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KondoInstance, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KondoInstance, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ftdic"] = _pykondo.KondoInstance_ftdic_set
    __swig_getmethods__["ftdic"] = _pykondo.KondoInstance_ftdic_get
    if _newclass:ftdic = _swig_property(_pykondo.KondoInstance_ftdic_get, _pykondo.KondoInstance_ftdic_set)
    __swig_setmethods__["swap"] = _pykondo.KondoInstance_swap_set
    __swig_getmethods__["swap"] = _pykondo.KondoInstance_swap_get
    if _newclass:swap = _swig_property(_pykondo.KondoInstance_swap_get, _pykondo.KondoInstance_swap_set)
    __swig_setmethods__["error"] = _pykondo.KondoInstance_error_set
    __swig_getmethods__["error"] = _pykondo.KondoInstance_error_get
    if _newclass:error = _swig_property(_pykondo.KondoInstance_error_get, _pykondo.KondoInstance_error_set)
    __swig_setmethods__["opt"] = _pykondo.KondoInstance_opt_set
    __swig_getmethods__["opt"] = _pykondo.KondoInstance_opt_get
    if _newclass:opt = _swig_property(_pykondo.KondoInstance_opt_get, _pykondo.KondoInstance_opt_set)
    __swig_setmethods__["debug"] = _pykondo.KondoInstance_debug_set
    __swig_getmethods__["debug"] = _pykondo.KondoInstance_debug_get
    if _newclass:debug = _swig_property(_pykondo.KondoInstance_debug_get, _pykondo.KondoInstance_debug_set)
    def __init__(self): 
        this = _pykondo.new_KondoInstance()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pykondo.delete_KondoInstance
    __del__ = lambda self : None;
KondoInstance_swigregister = _pykondo.KondoInstance_swigregister
KondoInstance_swigregister(KondoInstance)


def kondo_init(*args):
  return _pykondo.kondo_init(*args)
kondo_init = _pykondo.kondo_init

def kondo_init_custom(*args):
  return _pykondo.kondo_init_custom(*args)
kondo_init_custom = _pykondo.kondo_init_custom

def kondo_close(*args):
  return _pykondo.kondo_close(*args)
kondo_close = _pykondo.kondo_close

def kondo_write(*args):
  return _pykondo.kondo_write(*args)
kondo_write = _pykondo.kondo_write

def kondo_read(*args):
  return _pykondo.kondo_read(*args)
kondo_read = _pykondo.kondo_read

def kondo_read_timeout(*args):
  return _pykondo.kondo_read_timeout(*args)
kondo_read_timeout = _pykondo.kondo_read_timeout

def kondo_purge(*args):
  return _pykondo.kondo_purge(*args)
kondo_purge = _pykondo.kondo_purge

def kondo_trx(*args):
  return _pykondo.kondo_trx(*args)
kondo_trx = _pykondo.kondo_trx

def kondo_ack(*args):
  return _pykondo.kondo_ack(*args)
kondo_ack = _pykondo.kondo_ack

def kondo_get_options(*args):
  return _pykondo.kondo_get_options(*args)
kondo_get_options = _pykondo.kondo_get_options

def kondo_play_motion(*args):
  return _pykondo.kondo_play_motion(*args)
kondo_play_motion = _pykondo.kondo_play_motion

def kondo_stop_motion(*args):
  return _pykondo.kondo_stop_motion(*args)
kondo_stop_motion = _pykondo.kondo_stop_motion

def kondo_krc3_buttons(*args):
  return _pykondo.kondo_krc3_buttons(*args)
kondo_krc3_buttons = _pykondo.kondo_krc3_buttons

def kondo_read_analog(*args):
  return _pykondo.kondo_read_analog(*args)
kondo_read_analog = _pykondo.kondo_read_analog

def kondo_set_pio_direction(*args):
  return _pykondo.kondo_set_pio_direction(*args)
kondo_set_pio_direction = _pykondo.kondo_set_pio_direction

def kondo_get_pio_direction(*args):
  return _pykondo.kondo_get_pio_direction(*args)
kondo_get_pio_direction = _pykondo.kondo_get_pio_direction

def kondo_read_pio(*args):
  return _pykondo.kondo_read_pio(*args)
kondo_read_pio = _pykondo.kondo_read_pio

def kondo_write_pio(*args):
  return _pykondo.kondo_write_pio(*args)
kondo_write_pio = _pykondo.kondo_write_pio

def kondo_set_counter(*args):
  return _pykondo.kondo_set_counter(*args)
kondo_set_counter = _pykondo.kondo_set_counter

def kondo_get_counter(*args):
  return _pykondo.kondo_get_counter(*args)
kondo_get_counter = _pykondo.kondo_get_counter

def kondo_send_ics_pos(*args):
  return _pykondo.kondo_send_ics_pos(*args)
kondo_send_ics_pos = _pykondo.kondo_send_ics_pos

def kondo_get_servo_data(*args):
  return _pykondo.kondo_get_servo_data(*args)
kondo_get_servo_data = _pykondo.kondo_get_servo_data

def kondo_get_servo_trim(*args):
  return _pykondo.kondo_get_servo_trim(*args)
kondo_get_servo_trim = _pykondo.kondo_get_servo_trim

def kondo_get_servo_setpos(*args):
  return _pykondo.kondo_get_servo_setpos(*args)
kondo_get_servo_setpos = _pykondo.kondo_get_servo_setpos

def kondo_get_servo_pos(*args):
  return _pykondo.kondo_get_servo_pos(*args)
kondo_get_servo_pos = _pykondo.kondo_get_servo_pos

def kondo_get_servo_id(*args):
  return _pykondo.kondo_get_servo_id(*args)
kondo_get_servo_id = _pykondo.kondo_get_servo_id

def kondo_hareket(*args):
  return _pykondo.kondo_hareket(*args)
kondo_hareket = _pykondo.kondo_hareket

def kondo_set_servo_pos(*args):
  return _pykondo.kondo_set_servo_pos(*args)
kondo_set_servo_pos = _pykondo.kondo_set_servo_pos

def kondo_checksum(*args):
  return _pykondo.kondo_checksum(*args)
kondo_checksum = _pykondo.kondo_checksum

def kondo_verify_checksum(*args):
  return _pykondo.kondo_verify_checksum(*args)
kondo_verify_checksum = _pykondo.kondo_verify_checksum

def kondo_load_asciihex(*args):
  return _pykondo.kondo_load_asciihex(*args)
kondo_load_asciihex = _pykondo.kondo_load_asciihex
ICS_BAUD = _pykondo.ICS_BAUD
ICS_USB_VID = _pykondo.ICS_USB_VID
ICS_USB_PID = _pykondo.ICS_USB_PID
ICS_RX_TIMEOUT = _pykondo.ICS_RX_TIMEOUT
ICS_POS_TIMEOUT = _pykondo.ICS_POS_TIMEOUT
ICS_GET_TIMEOUT = _pykondo.ICS_GET_TIMEOUT
ICS_SET_TIMEOUT = _pykondo.ICS_SET_TIMEOUT
ICS_ID_TIMEOUT = _pykondo.ICS_ID_TIMEOUT
ICS_CMD_POS = _pykondo.ICS_CMD_POS
ICS_CMD_GET = _pykondo.ICS_CMD_GET
ICS_CMD_SET = _pykondo.ICS_CMD_SET
ICS_CMD_ID = _pykondo.ICS_CMD_ID
ICS_SC_EEPROM = _pykondo.ICS_SC_EEPROM
ICS_SC_STRETCH = _pykondo.ICS_SC_STRETCH
ICS_SC_SPEED = _pykondo.ICS_SC_SPEED
ICS_SC_CURRENT = _pykondo.ICS_SC_CURRENT
ICS_SC_READ = _pykondo.ICS_SC_READ
ICS_SC_WRITE = _pykondo.ICS_SC_WRITE
class ICSData(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ICSData, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ICSData, name)
    __repr__ = _swig_repr
    __swig_setmethods__["ftdic"] = _pykondo.ICSData_ftdic_set
    __swig_getmethods__["ftdic"] = _pykondo.ICSData_ftdic_get
    if _newclass:ftdic = _swig_property(_pykondo.ICSData_ftdic_get, _pykondo.ICSData_ftdic_set)
    __swig_setmethods__["swap"] = _pykondo.ICSData_swap_set
    __swig_getmethods__["swap"] = _pykondo.ICSData_swap_get
    if _newclass:swap = _swig_property(_pykondo.ICSData_swap_get, _pykondo.ICSData_swap_set)
    __swig_setmethods__["error"] = _pykondo.ICSData_error_set
    __swig_getmethods__["error"] = _pykondo.ICSData_error_get
    if _newclass:error = _swig_property(_pykondo.ICSData_error_get, _pykondo.ICSData_error_set)
    __swig_setmethods__["debug"] = _pykondo.ICSData_debug_set
    __swig_getmethods__["debug"] = _pykondo.ICSData_debug_get
    if _newclass:debug = _swig_property(_pykondo.ICSData_debug_get, _pykondo.ICSData_debug_set)
    def __init__(self): 
        this = _pykondo.new_ICSData()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pykondo.delete_ICSData
    __del__ = lambda self : None;
ICSData_swigregister = _pykondo.ICSData_swigregister
ICSData_swigregister(ICSData)


def ics_init(*args):
  return _pykondo.ics_init(*args)
ics_init = _pykondo.ics_init

def ics_close(*args):
  return _pykondo.ics_close(*args)
ics_close = _pykondo.ics_close

def ics_write(*args):
  return _pykondo.ics_write(*args)
ics_write = _pykondo.ics_write

def ics_read(*args):
  return _pykondo.ics_read(*args)
ics_read = _pykondo.ics_read

def ics_read_timeout(*args):
  return _pykondo.ics_read_timeout(*args)
ics_read_timeout = _pykondo.ics_read_timeout

def ics_purge(*args):
  return _pykondo.ics_purge(*args)
ics_purge = _pykondo.ics_purge

def ics_trx(*args):
  return _pykondo.ics_trx(*args)
ics_trx = _pykondo.ics_trx

def ics_trx_timeout(*args):
  return _pykondo.ics_trx_timeout(*args)
ics_trx_timeout = _pykondo.ics_trx_timeout

def ics_pos(*args):
  return _pykondo.ics_pos(*args)
ics_pos = _pykondo.ics_pos

def ics_hold(*args):
  return _pykondo.ics_hold(*args)
ics_hold = _pykondo.ics_hold

def ics_free(*args):
  return _pykondo.ics_free(*args)
ics_free = _pykondo.ics_free

def ics_get_stretch(*args):
  return _pykondo.ics_get_stretch(*args)
ics_get_stretch = _pykondo.ics_get_stretch

def ics_get_speed(*args):
  return _pykondo.ics_get_speed(*args)
ics_get_speed = _pykondo.ics_get_speed

def ics_get_current(*args):
  return _pykondo.ics_get_current(*args)
ics_get_current = _pykondo.ics_get_current

def ics_set_stretch(*args):
  return _pykondo.ics_set_stretch(*args)
ics_set_stretch = _pykondo.ics_set_stretch

def ics_set_speed(*args):
  return _pykondo.ics_set_speed(*args)
ics_set_speed = _pykondo.ics_set_speed

def ics_set_current_limit(*args):
  return _pykondo.ics_set_current_limit(*args)
ics_set_current_limit = _pykondo.ics_set_current_limit

def ics_get_id(*args):
  return _pykondo.ics_get_id(*args)
ics_get_id = _pykondo.ics_get_id

def ics_set_id(*args):
  return _pykondo.ics_set_id(*args)
ics_set_id = _pykondo.ics_set_id
# This file is compatible with both classic and new-style classes.


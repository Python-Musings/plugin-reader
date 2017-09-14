class FileData(object):
    """ FileData:
    signature     '4s' : name of record, also record type
    data_size     'I' : size of record

    :Vars:
    magic_number : number of bytes for all records.
                 : Oblivion is 20 all other games use 24
    tes4_sig     : plugin header signature
    group_sig    : Group signature, is not the signature of the groups that
                 : follow, only indicated the beginning of a Group
    """
    magic_number = 24
    tes4_sig = 'TES4'
    group_sig = 'GRUP'

    def __init__(self):
        self.signature
        self.data_size

    @staticmethod
    def unpack(ins):
        """Return a RecordHeader object by reading the input stream."""
        raise exception.AbstractError

    def pack(self):
        """Return the record header packed into a string to be written to file"""
        raise exception.AbstractError

class FileGroup(FileData):
    """ FileRecord:
    :Inherits: FileData
    signature     '4s' : name of record, also record type
    data_size      'I' : size of record

    :New Instances:
    group_name    '4s' : signature of following groups i.e. GMST, KYWD
    group_type     'I' : group type 1, 10
    time_stamp     'H' : presumed to be a time stamp
    grec_unk_one   'H' : presumed to be creation kit version control
    form_version   'H' : version of the record format
    grec_unk_two   'H' : presumed to be creation kit version control
    record_data        : the records sub groups (data_size - 24)
    """

    def __init__(self):
        super(FileGroup, self).__init__(self)
        self.group_name
        self.group_type
        self.time_stamp
        self.grec_unk_one
        self.form_Version
        self.grec_unk_two
        self.group_data

class FileRecord(FileGroup):
    """ FileRecord:
    :Inherits: FileData
    signature    '4s' : name of record, also record type
    data_size     'I' : size of record

    :New Instances:
    record_flags  'I' : flags set for the record
    next_form     'I' : next form available
    vrec_info_one 'I' : presumed to be creation kit version control
    form_version  'H' : version of the record format
    vrec_info_two 'H' : presumed to be creation kit version control
    record_data       : the records data

    when record_flags & 0b00040000 the data is compressed

    decompressed_size 'I' : size of decompressed data
    record_data           : compressed data of (data_size - 4) with zlib
    """

    def __init__(self):
        super(FileRecord, self).__init__(self)
        self.record_flags
        self.next_form
        self.vrec_info_one
        self.form_version
        self.vrec_info_two
        self.record_data

class DataField(FileRecord):
    """ FileRecord:
    :Inherits: FileData
    signature     '4s' : name of record, also record type
    data_size      'I' : size of record

    :New Instances:
    field_data         : field data of data_size

    :Special Cases:
    XXXX : Is used when ANY subrecord's size exceeds 65535.
         : data_size it the size of data that follows XXXX
         : field_data will be null and data will have the
         : four letter signature of the data XXXX is prepended
         : to, and uses the signature of a subrecord.
    """
    def __init__(self):
        super(DataField, self).__init__(self)
        self.field_data


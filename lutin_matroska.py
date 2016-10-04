#!/usr/bin/python
import lutin.debug as debug
import lutin.tools as tools


def get_type():
	return "LIBRARY"

def get_desc():
	return "matroska library Muxer and deMuxer matroska tool"

def get_licence():
	return "LGPL-2.1"

def get_maintainer():
	return ["Moritz Bunkus <moritz@bunkus.org>"]

def get_version():
	return [1,4,4]

def configure(target, my_module):
	my_module.add_src_file([
	    'matroska/src/KaxInfoData.cpp',
	    'matroska/src/KaxCluster.cpp',
	    'matroska/src/KaxContexts.cpp',
	    'matroska/src/KaxSeekHead.cpp',
	    'matroska/src/KaxSegment.cpp',
	    'matroska/src/KaxAttachments.cpp',
	    'matroska/src/FileKax.cpp',
	    'matroska/src/KaxSemantic.cpp',
	    'matroska/src/KaxAttached.cpp',
	    'matroska/src/KaxTracks.cpp',
	    'matroska/src/KaxBlock.cpp',
	    'matroska/src/KaxCues.cpp',
	    'matroska/src/KaxCuesData.cpp',
	    'matroska/src/KaxVersion.cpp',
	    'matroska/src/KaxBlockData.cpp',
	    ])
	my_module.add_header_file([
	    'matroska/matroska/KaxTag.h',
	    'matroska/matroska/KaxConfig.h',
	    'matroska/matroska/KaxTypes.h',
	    'matroska/matroska/KaxChapters.h',
	    'matroska/matroska/KaxTrackAudio.h',
	    'matroska/matroska/KaxDefines.h',
	    'matroska/matroska/KaxContexts.h',
	    'matroska/matroska/KaxContentEncoding.h',
	    'matroska/matroska/KaxSegment.h',
	    'matroska/matroska/KaxCluster.h',
	    'matroska/matroska/KaxTags.h',
	    'matroska/matroska/KaxSeekHead.h',
	    'matroska/matroska/KaxVersion.h',
	    'matroska/matroska/KaxCuesData.h',
	    'matroska/matroska/KaxBlock.h',
	    'matroska/matroska/FileKax.h',
	    'matroska/matroska/KaxBlockData.h',
	    'matroska/matroska/KaxAttachments.h',
	    'matroska/matroska/KaxInfoData.h',
	    'matroska/matroska/KaxTracks.h',
	    'matroska/matroska/KaxTrackEntryData.h',
	    'matroska/matroska/KaxTrackVideo.h',
	    'matroska/matroska/KaxCues.h',
	    'matroska/matroska/KaxInfo.h',
	    'matroska/matroska/KaxAttached.h',
	    'matroska/matroska/KaxClusterData.h',
	    'matroska/matroska/KaxSemantic.h',
	    ],
	    destination_path="matroska")
	my_module.add_header_file([
	    'matroska/matroska/c/libmatroska.h',
	    'matroska/matroska/c/libmatroska_t.h',
	    ],
	    destination_path="matroska/c")
	my_module.add_depend([
	    'cxx',
	    'ebml'
	    ])
	my_module.compile_version("C++", 2003)
	return True



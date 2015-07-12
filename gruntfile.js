module.exports = function(grunt) {

  grunt.initConfig({
    watch: {
    	textToNumber: {
	      files: ['*.py'],
	      tasks: ['shell:textToNumber']
	  	},
    	textToDate: {
	      files: ['*.py'],
	      tasks: ['shell:textToDate']
    	},
    },
    shell: {
     	textToNumber: {
        command: 'python textToNumberConverter/main_test.py'
      },
     	textToDate: {
        command: 'python textToDateConverter/main_test.py'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', ['shell:textToNumber']);
};

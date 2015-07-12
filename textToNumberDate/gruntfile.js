module.exports = function(grunt) {

  grunt.initConfig({
    watch: {
      files: ['*.py'],
      tasks: ['shell']
    },
    shell: {
      test: {
        command: 'python main_test.py'
      }
    }
  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-shell');

  grunt.registerTask('default', ['watch']);
};

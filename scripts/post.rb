#! /usr/bin/env ruby
require 'yaml'
require 'highline'
require 'active_support/all'
require 'ostruct'
require 'stringex_lite'
class Answers
  attr :title, :tags, :categories, :file_string, :date_string, :dt_string, :layout, :file_type
  def initialize
    @title = nil
    @tags = nil
    @categories = nil

    @file_string = nil
    @date_string = nil
    @dt_string = nil
    @layout = 'post' # Script is post.rb
    @file_type = nil
    # TODO: require a 'post.rb', 'page.rb', 'draft.rb' with questions
  end
  def set_time_zone(time_zone)
    Time.zone = time_zone
    @dt_string = Time.zone.now
  end
  def set_date_string
    @date_string = dt_string.strftime('%Y-%m-%d')
  end
  def set_file_string
    @file_string = @date_string + '-' + @title.to_url
  end
  def set_title(title)
    @title = title
  end
  def set_tags(tag_array)
    @tags = tag_array
  end
  def set_published(bool)
    @published = bool
  end
  def set_categories(categories)
    @categories = categories
  end
  def set_file_type(type)
    @file_type = type
  end
  def dump
    f = OpenStruct.new
    if @layout
      f['layout'] = @layout
    end
    if @title
      f['title'] = "#{@title}"
    end
    if @date_string
      f['date'] = "#{@dt_string}"
    end
    if @tags
      f['tags'] = @tags
    end
    if @published
      f['published'] = @published
    end
    if @categories
      f['categories'] = @categories
    end
    f.methods
    puts f.to_h.stringify_keys.to_yaml
    puts '---'
  end
end
$answers = Answers.new
$cli = HighLine.new

def ask_questions
  $cli.say "Starting 'post.rb'..."
  $cli.say "This will only make posts for '_posts' not '_drafts' or pages (currently)"
end
def whats_your_time_zone
  timezone = $cli.choose do |menu|
    menu.header = 'Select your Time Zone'
    menu.choice :Eastern_Time, "Eastern Time"
    menu.choice :Central_Time, "Central Time"
    menu.prompt = "Selection: "
  end
  case timezone
    when :Eastern_Time
      $answers.set_time_zone('Eastern Time (US & Canada)')
      $answers.set_date_string
    when :Central_Time
      $answers.set_time_zone('Central Time (US & Canada)')
      $answers.set_date_string
  end
end
def get_title
  title = $cli.ask("Title: ", String)
  $answers.set_title(title)
end
def get_tags
  tags = $cli.ask "Tags:" do |m|
    m.gather = '.'
  end
  $answers.set_tags(tags)
end
def get_categories
  categories = $cli.ask "Categories:" do |m|
    m.gather = '.'
  end
  $answers.set_categories(categories)
end
def publish?
  publish = $cli.agree("Do you want to publish this post immediately? ", true)
  case publish
    when true
      $answers.set_published(true)
    when false
      $answers.set_published(false)
  end
end

def main
  ask_questions
  whats_your_time_zone
  get_title
  get_tags
  get_categories
  publish?
  output = $cli.choose do |menu|
    menu.header = "How would you like to output this front matter"
    menu.choice :file
    menu.choice :stdout
    menu.prompt = "? "
  end
  file_type = $cli.choose do |menu|
    menu.header = "What file format?"
    menu.choice :md
    menu.choice :html
    menu.prompt = "? "
  end
  case file_type
    when :md
      $answers.set_file_type('.md')
    when :html
      $answers.set_file_type('.html')
  end
  case output
    when :file
      $answers.set_file_string
      puts $answers.file_string + $answers.file_type
    when :stdout
      $answers.dump
  end

end
main if __FILE__ =~ /^.*\/post.rb$/
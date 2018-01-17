#! /usr/bin/env ruby
require 'yaml'
require 'highline'
require 'active_support/all'
require 'ostruct'
class Answers
  attr :title, :tags, :categories, :published, :file_string, :date_string, :dt_string
  def initialize
    @title = nil
    @tags = nil
    @categories = nil

    @file_string = nil
    @date_string = nil
    @dt_string = nil
  end
  def set_time_zone(time_zone)
    Time.zone = time_zone
    @date_string = Time.zone.now
  end
  def set_title(title)
    @title = title
  end
  def set_tags(tag_array)
    @tags = tag_array
  end
  def set_published(how)
    @published
  end
  def dump(file)
    f = OpenStruct.new
    if @title
      f['title'] = "#{@title}"
    end
    if @date_string
      f['date'] = "#{@date_string}"
    end
    if @tags
      f['tags'] = @tags
    end
    if @published
      f['publish'] = @published
      if @published == :"Draft"

      end
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
    when :Central_Time
      $answers.set_time_zone('Central Time (US & Canada)')
  end
end
def get_title
  title = $cli.ask("Title: ", String)
  $answers.set_title(title)
end
def get_tags
  tags = $cli.ask "Tag Names?" do |m|
    m.gather = '.'
  end
  $answers.set_tags(tags)
end
def publish?
  publish = $cli.choose do |menu|
    menu.header = 'Select how you want to publish this post (number index or name)'
    menu.choice :"Publish"
    menu.choice :"Draft"
    menu.choice :"Neither_Do_Not_Publish"
    menu.prompt = "Selection: "
  end
  case publish
    when :"Publish"
      $answers.set_time_zone('Eastern Time (US & Canada)')
    when :"Draft"
      $answers.set_time_zone('Central Time (US & Canada)')
    when :"Neither_Do_Not_Publish"
  end
  end
end

def main
  ask_questions
  whats_your_time_zone
  get_title
  get_tags
  publish?
  $answers.dump(STDOUT)
end
main if __FILE__ =~ /^.*\/post.rb$/